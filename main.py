import requests


#--------------------------CARGAMOS EL JSON--------------------------


# URL de la API que contiene el archivo JSON
url = 'https://api.sampleapis.com/beers/ale'

try:
    # Guardamos la URL en una variable
    response = requests.get(url)

    # Comprobamos si la URL está operativa, si no, devuelve un error
    if response.status_code == 200:
        data = response.json()

    # Aquí se muestra el error que devuelve la API en caso de fallar
    else:
        print('Error al hacer la solicitud a la API:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Error de conexión:', e)          # Envolvemos todo en un TRY - EXCEPT para contemplar errores


#--------------------------MOSTRAMOS DATOS--------------------------


nombreCerveza = str(input("Busca cerveza por su nombre"))
cervezaEncontrada = " "

for cerveza in data:
    if cerveza.get("name") == nombreCerveza:
        cervezaEncontrada = cerveza
        break

if cervezaEncontrada:
    # Ahora 'objeto_deseado' contiene el objeto con el nombre buscado
    print(cervezaEncontrada)
else:
    print(f"No se encontró ningún objeto con el nombre '{nombreCerveza}'")
