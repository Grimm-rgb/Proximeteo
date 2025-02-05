import datetime
import sys
import threading
import time
import requests
import json
import prelevement
import random
import statistics

class Sonde() :
    baseUrl = "http://10.121.128.165:5000/"   
    # url du sites
    idSonde= ""         
    #id de la sonde, dans notre cas ça correspond à l'adresse i2c de la sonde
    
    # isActive = False  
    #sert à indiquer au thread de se fermer

    def __init__(self, sonde) :
        self.idSonde = sonde

    def close(self):
        return self.isActive

    def run(self) :
        print('Prélèvement : ')
        
        # Vérifie si la sonde est activée
        # if self.isActive:
        
        # récupération des valeurs
        p = self.fakePrelevement()
        date = str(datetime.datetime.now())

        r = requests.post(self.baseUrl + '/re', json={
            "temperature": p.temperature,
            "humidite": p.humidite,
            "sonde_id": str(self.idSonde),
            "date": date
        })
        print(f"Status Code: {r.status_code}, Response: {r.json()}")
    
    # génère des données
    def fakePrelevement(self) :
        listT = []
        listH = []
        n = 5
        i = 0
        rate = 0.5

        while i < n:
            listT.append(random.randint(-5, 40))
            listH.append(random.randint(0, 100))
            i += 1
            print(i)
            time.sleep(rate)

        return prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH))