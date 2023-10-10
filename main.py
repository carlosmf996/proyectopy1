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

# Pedimos los datos al usuario por consola y los mostramos
nombreCerveza = str(input("Busca cerveza por su nombre: "))
cervezaEncontrada = ""
encontrada = False
indice=0

while indice<len(data) and encontrada == False:
    if data[indice].get("name") == nombreCerveza:
        cervezaEncontrada = data[indice]
        encontrada=True
    else:
        indice+=1

if cervezaEncontrada != "":
    print(cervezaEncontrada)
else:
    print("No se encontró ningún objeto con el nombre ", nombreCerveza)
