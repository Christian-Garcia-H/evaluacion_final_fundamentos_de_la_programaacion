#paleta de colores
RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
BLANCO = "\033[97m"
NEGRITA = "\033[1m"
# Variables con colores
ERROR = "\033[1;31m"
EXITO = "\033[1;32m"
MENU = "\033[1;36m"
TITULO = "\033[1;34m"
AVISO = "\033[1;33m"
# Matriz inicial: [ID_Cliente, Duracion_segundos, Clics]
datos = [
    ["C001", 210, 12],
    ["C002", 45, 5],
    ["C003", 120, 6],
    ["C004", 200, 2],
    ["C005", 150, 7]
]


print(TITULO + r"""
 ____                                                       __            
/\  _`\    __                                        __    /\ \           
\ \ \L\ \ /\_\     __    ___   __  __     __    ___ /\_\   \_\ \    ___   
 \ \  _ <'\/\ \  /'__`\/' _ `\/\ \/\ \  /'__`\/' _ `\/\ \  /'_` \  / __`\ 
  \ \ \L\ \\ \ \/\  __//\ \/\ \ \ \_/ |/\  __//\ \/\ \ \ \/\ \L\ \/\ \L\ \
   \ \____/ \ \_\ \____\ \_\ \_\ \___/ \ \____\ \_\ \_\ \_\ \___,_\ \____/
    \/___/   \/_/\/____/\/_/\/_/\/__/   \/____/\/_/\/_/\/_/\/__,_ /\/___/ 
------------Calcula el compromiso de tus clientes en instantes------------
""" + RESET)


#funcion para calcular el compromiso de los clientes:
def calcular_compromiso (duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"
    
#imprimir informe total    
def informe_total():
    for cliente in datos:
       id_cliente = cliente[0]
       duracion = cliente[1]
       clics = cliente[2]
       compromiso = calcular_compromiso(duracion, clics)
       print(f"El compromiso del usuario {id_cliente} fue: {compromiso}")

#Agregar datos al registro de duración y clics    
def agregar_registro(datos):
    ultimo_id = datos[-1][0]
    numero = int(ultimo_id[3:]) + 1
    nuevo_id = "C" + str(numero).zfill(3)
    datos.append([nuevo_id, duracion, clics])
    print("\nRegistro agregado correctamente.")
    print("Nuevo registro:", datos[-1])

#Eliminar datos del registro por ID
def eliminar_registro(datos, id_buscado):
    for i in range(len(datos)):
        if datos[i][0] == id_buscado:
            datos.pop(i)
            print("Registro eliminado correctamente.")
            return True
    print(f"{ERROR}No existe un registro con ese ID. Prueba con un ID como: C001{RESET}")
    return False

#Imprimir informe por ID
def informe_por_id(datos, id_cliente):
    for cliente in datos:
        if cliente[0] == id_cliente:
            duracion = cliente[1]
            clics = cliente[2]
            compromiso = calcular_compromiso(duracion, clics)

            print(f"El compromiso del usuario {id_cliente} fue: {compromiso}")
            return True

    print(f"{ERROR}No existe un registro con ese ID. Prueba con un ID como: C001{RESET}")
    return False
    
#bucle principal del programa
while True:
    print(f"\n{MENU}================================================={RESET}")
    print(f"{TITULO}               MENÚ PRINCIPAL{RESET}")
    print(f"{MENU}================================================={RESET}")
    print(f"{AZUL}1.{RESET} Imprimir informe completo de compromiso")
    print(f"{AZUL}2.{RESET} Agregar datos al registro de duración y clics")
    print(f"{AZUL}3.{RESET} Eliminar datos del registro por ID")
    print(f"{AZUL}4.{RESET} Imprimir informe por ID")
    print(f"{MENU}-------------------------------------------------{RESET}")
    intentos = 0
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-4): "))

            if 1 <= opcion <= 4:
                break
            else:
                print(f"{ERROR}Error: Debe ingresar un número entre 1 y 4.{RESET}")
                intentos += 1

        except ValueError:
            print(f"{ERROR}Error: Debe ingresar únicamente un número entero.{RESET}")
            intentos += 1

        if intentos == 3:
            print(f"\n{AVISO}Ha agotado los 3 intentos. Se mostrará nuevamente el menú.{RESET}\n")
            break
    if intentos == 3:
        continue
    #imprimir informe total  
    if opcion == 1:
        informe_total()
    elif opcion == 2:
        # Entrada de tiempo en segundos
        while True:
            try:
                duracion = int(input("Ingrese la duración (segundos): "))
                if duracion > 0:
                     break
                else:
                     print(f"{ERROR}La duración no puede ser negativa.{RESET}")
            except ValueError:
                print(f"{ERROR}Debe ingresar un número entero.{RESET}")
        # Entrada de numero de clics
        while True:
            try:
                 clics = int(input("Ingrese la cantidad de clics: "))
                 if clics >= 0:
                   break
                 else:
                    print(f"{ERROR}Los clics no pueden ser negativos.{RESET}")
            except ValueError:
                    print(f"{ERROR}Debe ingresar un número entero.{RESET}")
        #agrega nuevo registro al final de la matriz
        agregar_registro(datos)
    elif opcion == 3:
        while True:
            try:
                id_buscado = input("Ingrese el ID del registro a eliminar: ").upper()
                if id_buscado == "":
                     raise ValueError
                if eliminar_registro(datos, id_buscado):
                     break
            except ValueError:
                print(f"{ERROR}Debe ingresar un ID válido.{RESET}")
    elif opcion == 4:
        while True:
             try:
                 id_buscado = input("Ingrese el ID del cliente: ").upper()
                 if id_buscado == "":
                   raise ValueError
                 if informe_por_id(datos, id_buscado):
                   break
             except ValueError:
                 print(f"{ERROR}Debe ingresar un ID válido.{RESET}")
    