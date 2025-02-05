#from sonde import *
from fakeSonde import *
import time
import requests
import json

baseUrl = " http://127.0.0.1:8000"


#Récupération des id des sondes présentent dans la table sonde
jsonSonde = requests.get(baseUrl + '/sonde')
data = json.loads(jsonSonde.content)
list = []
i = 0
for d in data:
    print("sonde : ", d)
    s = Sonde(d["id"], 0x76)
    list.append(s)
    
#Consulte la table Sonde de la BDD pour savoir si la sonde est activée ou non
# def is_active(idSonde) :
    # check = requests.get(baseUrl + "/sonde/" + idSonde)
    # return check.json()["activate"]


#boucle principale de gestion de l'activité des sondes 
# while len(list) > 0 :
#     try :
#         for t in list :
#             #Vérifie si la sonde est désactivée alors qu'elle est active sur la table Sonde dans la BDD
#             if t.isActive == False and is_active(t.idSonde) :
#                 t.isActive = True
#                 print("Relance la sonde")
#             #Vérifie si la sonde est désactivée en consultant la table Sonde dans la BDD
#             if is_active(t.idSonde) == False:
#                 t.isActive = False
#                 print("La sonde est inactive")
                        
                        
#         time.sleep(1)
#     except Exception as e:
#         print('An unexpected error occurred:', str(e))
#         break