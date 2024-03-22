#get all data about comets.

import requests
import os

os.system('clear')
def get_comets():
    global count 
    print(":::COMETS INFORMATION:::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    
    try:
        #petición ala API
         response = requests.get(url)
         response.raise_for_status()
         count = 0
         planet = input("Escriba el nombre del planeta: ")
         #total = int(input("Cantidad de datos a mostrar: "))

         data = response.json() #convierte en formato JSON
         #imprimir todos los nombres de cometas
         for comet in data["bodies"]:
              if comet ["englishName"] == planet:
              #if comet["isPlanet"] == True:
                print("English Name: ", comet["englishName"])
                print("moons: ", comet["moons"])
                print("gravity: ", comet["gravity"])
                print("Is planet?: ", comet["isPlanet"])
                print("\n")

                #count = count +1

             # if count == total:
                 #  break


    except requests.exceptions.RequestException as e:
         print(f"API Error: {e}")

get_comets()
#print("Total de datos: ",count)



