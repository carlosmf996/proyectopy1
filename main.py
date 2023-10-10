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
nombreCerveza = str(input("Busca cerveza por su nombre: ")).upper()
cervezaEncontrada = ""
encontrada = False
indice=0

# Hacer búsquedas con un FOR es bastante poco eficaz por lo que busco con un WHILE
while indice<len(data) and encontrada == False:
    if data[indice].get("name").upper() == nombreCerveza:
        cervezaEncontrada = data[indice]
        encontrada=True
    else:
        indice+=1

if cervezaEncontrada != "":
    print("NOMBRE: ",cervezaEncontrada.get("name"))
    print("PRECIO: ",cervezaEncontrada.get("price"))
    print("NOTA:")
    print("   Nº RESEÑAS",cervezaEncontrada.get("rating").get("reviews"))
    media = cervezaEncontrada.get("rating").get("average")
    mostrarMedia = f"{media:.2f}"
    print("   NOTA", mostrarMedia)


else:
    print("No se encontró ningún objeto con el nombre ", nombreCerveza)
