#Simplifie la transmission des résultats de la sonde 
class Prelevement() :
    temperature = 0
    humidity = 0
    
    def __init__(self) :
        self.temperature = 0
        self.humidity = 0

    def __init__(self, t, h) :
        self.temperature = t
        self.humidity = h

    def add(self, prelevement) :
        self.temperature = prelevement.temperature
        self.humidity = prelevement.humidite