import requests


#--------------------------CARGAMOS EL JSON--------------------------


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
        #print(data)
    else:
        print('Error al hacer la solicitud a la API:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Error de conexión:', e)


#--------------------------MOSTRAMOS DATOS--------------------------


nombre_buscar = "Founders All Day IPA"  # Reemplaza con el nombre que deseas buscar
objeto_deseado = None

for elemento in data:
    if elemento.get("name") == nombre_buscar:
        objeto_deseado = elemento
        break

if objeto_deseado:
    # Ahora 'objeto_deseado' contiene el objeto con el nombre buscado
    print(objeto_deseado)
else:
    print(f"No se encontró ningún objeto con el nombre '{nombre_buscar}'")
