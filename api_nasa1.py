#API: application programming interface
#NASA: Get comets: https://api.nasa.gov/
#API_KEY_NASA: tcm1FybTRNHgoqXsV0zJEO3RATnQdh7plZ2BNW5g
#developer: Joan C. Ayala
#data: 20242401
#script description: Get data from Nasa API about comets

import requests 
import os

os.system('clear')
def get_comet_data(api_key):
    print("::: COMET INFORMATION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try: 
        #Realizar la solicitud a la api
        response = requests.get(url)
        response.raise_for_status() #valida si se presento algun error en la peteción
        #convertir la respuesta de la peticion a formato JSON(js object natation)
        datos = response.json()

        print(f"Comet name: {datos['name']}")
        print(f"Absolute magnitude: {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter max (KM): {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter max (FT): {datos['estimated_diameter']['feet']['estimated_diameter_max']}")
        
    except requests.exceptions.RequestException as e :
        print(f"Error al realizar la petición a la API de NASA: {e}")

api_key_nasa = 'tcm1FybTRNHgoqXsV0zJEO3RATnQdh7plZ2BNW5g'
get_comet_data(api_key_nasa)



