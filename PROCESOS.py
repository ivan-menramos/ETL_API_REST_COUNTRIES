import pandas as pd
import requests

"""def extraer_datos():
	url = api_url"""
	
pais = "mexico"
url = f"https://restcountries.com/v3.1/name/{pais}"
respuesta = requests.get(url)
datos = respuesta.json()
print(datos)
