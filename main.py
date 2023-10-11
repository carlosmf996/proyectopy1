import requests
import math

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




#--------------------------FUNCIONES--------------------------

def buscarNombre():     #Esta función permite la búsqueda de cervezas por nombre

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

    # Doy formato a la información mostrada
    if cervezaEncontrada != "":
        print("")
        print("NOMBRE: ",cervezaEncontrada.get("name"))
        print("PRECIO: ",cervezaEncontrada.get("price"))
        print("NOTA:")
        print("   Nº RESEÑAS",cervezaEncontrada.get("rating").get("reviews"))
        media = cervezaEncontrada.get("rating").get("average")
        mostrarMedia = f"{media:.2f}"
        print("   NOTA", mostrarMedia)

    else:
        print("No se encontró la cerveza ", nombreCerveza)

    print("")
    continuar = input("¿Quieres buscar otra Cerveza?  S/N: ")    

    if continuar.upper() == "S":
        buscarNombre()
    else:
       mostrarMenu()


def buscarPrecio():     # Esta función permite buscar las cervezas menores al precio que indica el usuario

    cervezas_guardadas = []
    precio_maximo = 0  

    while precio_maximo == 0:       #Con este while controlamos que el usuario introduzca un float/int
        try:
            precioIntroducido = float(input("Precio máximo a pagar: $"))
            precio_maximo = precioIntroducido  # Asignamos el valor a precio_maximo
        except ValueError:
            print("Introduzca un valor correcto")


    for cerveza in data:  #Este bucle recorre todo el JSON guardando en nuestro nuevo diccionario las cervezas que e adaptan al precio dado
        precio_cerveza = float(cerveza.get("price").replace('$', ''))  # Convierte el precio en un número
        if precio_cerveza <= precio_maximo:
            cervezas_guardadas.append(cerveza)


    if cervezas_guardadas:
        for cerveza in cervezas_guardadas:              #Muestro las cervezas que ha encontrado el programa
            print("")
            print("NOMBRE: ",cerveza.get("name"))
            print("PRECIO: ",cerveza.get("price"))
            print("NOTA:")
            print("   Nº RESEÑAS",cerveza.get("rating").get("reviews"))
            media = cerveza.get("rating").get("average")
            mostrarMedia = f"{media:.2f}"
            print("   NOTA", mostrarMedia)
        else:
            print("No tenemos cervezas por ese precio")

    print("")
    continuar = input("¿Quieres comparar otro precio? (S/N): ")
    if continuar.upper() == "S":
        buscarPrecio()                  #Pequeña sentencia para controlar el movimiento por el menú
    else:
        mostrarMenu()


def buscarNota():

    cervezasGuardadasNota = []
    notaBuscar = 0

    while notaBuscar == 0:       #Con este while controlamos que el usuario introduzca un float/int
        try:
            notaIntroducida = float(input("Nota media a consultar: "))
            notaBuscar = notaIntroducida  # Asignamos el valor a notaBuscar
        except ValueError:
            print("Introduzca una nota correcto")

    for cerveza in data:
        if notaBuscar < cerveza.get("average").get("rating"):
            cervezasGuardadasNota.append(cerveza)

    if cervezasGuardadasNota:
        for cerveza in cervezasGuardadasNota:              #Muestro las cervezas que ha encontrado el programa
            print("")
            print("NOMBRE: ",cerveza.get("name"))
            print("PRECIO: ",cerveza.get("price"))
            print("NOTA:")
            print("   Nº RESEÑAS",cerveza.get("rating").get("reviews"))
            media = cerveza.get("rating").get("average")
            mostrarMedia = f"{media:.2f}"
            print("   NOTA", mostrarMedia)
        else:
            print("No tenemos cervezas por ese precio")                

    print("")
    continuar = input("¿Quieres comparar otra nota? (S/N): ")
    if continuar.upper() == "S":
        buscarPrecio()                  #Pequeña sentencia para controlar el movimiento por el menú
    else:
        mostrarMenu()


def mostrarMenu():          #Esta función muestra el menú por el que navegaremos

    print("")
    print("----------CERVECERIA LQTC----------")
    print("")
    print("1.- Búsqueda por nombre")
    print("2.- Búsqueda por precio")
    print("3.- Búsqueda por nota media")
    print("4.- Cervezas ordenadas por precio")
    print("5.- Cervezas ordenadas por nota media")
    print("6.- SALIR")
    print("")

    numeroMenu = int(input("Introduzca opción del menú: "))

    if numeroMenu > 6 or numeroMenu < 1:            #Controlamos que el número introducido sea correcto
        print("")
        print("INTRODUZCA UN NÚMERO CORRECTO")
        print("")
        mostrarMenu()

    if numeroMenu == 1:
        buscarNombre()

    if numeroMenu == 2:
        buscarPrecio()


    if numeroMenu == 6:
        print("¡¡¡Vuelve pronto!!!")
        exit        


#--------------------------EJECUTAMOS EL PROGRAMA--------------------------

mostrarMenu()