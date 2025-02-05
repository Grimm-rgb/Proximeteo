import sys
import time
import smbus2
import bme280
import requests
import time
import json
import prelevement
import random
import statistics
import datetime

baseUrl = "http://10.121.128.165:5000/"

def celsius(far):
        return ((far-32)*5)/9

def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
        
class Sonde() : # url du site
    address = 0x76
    idSonde= ""         #id de la sonde, dans notre cas ça correspond à l'adresse i2c de la sonde
    isActivate = False  #sert à indiquer au thread de se fermer
    # Initialize I2C bus
    bus = smbus2.SMBus(1)

    # Load calibration parameters
    calibration_params = bme280.load_calibration_params(bus, address)
        
    def __init__(self, sonde, address) :
        self.idSonde = sonde
        self.calibration_params = bme280.load_calibration_params(self.bus, address)

    def close(self):
        return self.isActivate

    def run(self) :
        # if self.isActivate:
        p = self.Prelevement()
        date = str(datetime.datetime.now())

        r = requests.post(baseUrl + '/re', json={
            "temperature": p.temperature,
            "humidite": p.humidite,
            "sonde_id": str(self.idSonde),
            "date": date
        })
        print(f"Status Code: {r.status_code}, Response: {r.json()}")
    
    def Prelevement(self) :  
        listT = []
        listH = []
        n = 5
        i = 0
        rate = 0.5

        while i < n:
            data = bme280.sample(self.bus, self.address, self.calibration_params)
            listT.append(data.temperature)
            listH.append(data.humidity)
            i += 1
            print(i)
            time.sleep(rate)
            
        return prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH))
    