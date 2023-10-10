import requests

# URL de la API que contiene el archivo JSON
url = 'https://api.sampleapis.com/beers/ale'

try:
    # Realizar la solicitud GET a la API
    response = requests.get(url)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Analizar la respuesta JSON
        data = response.json()

        # Ahora 'data' contiene el JSON cargado
        print(data)
    else:
        print('Error al hacer la solicitud a la API:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Error de conexión:', e)
