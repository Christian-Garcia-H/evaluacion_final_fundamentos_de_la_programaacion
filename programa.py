# Matriz inicial: [ID_Cliente, Duracion_segundos, Clics]
datos = [
    ["C001", 210, 12],
    ["C002", 45, 5],
    ["C003", 120, 6],
    ["C004", 200, 2],
    ["C005", 150, 7]
]


print(r"""
 ____                                                       __            
/\  _`\    __                                        __    /\ \           
\ \ \L\ \ /\_\     __    ___   __  __     __    ___ /\_\   \_\ \    ___   
 \ \  _ <'\/\ \  /'__`\/' _ `\/\ \/\ \  /'__`\/' _ `\/\ \  /'_` \  / __`\ 
  \ \ \L\ \\ \ \/\  __//\ \/\ \ \ \_/ |/\  __//\ \/\ \ \ \/\ \L\ \/\ \L\ \
   \ \____/ \ \_\ \____\ \_\ \_\ \___/ \ \____\ \_\ \_\ \_\ \___,_\ \____/
    \/___/   \/_/\/____/\/_/\/_/\/__/   \/____/\/_/\/_/\/_/\/__,_ /\/___/ 
------------Calcula el compromiso de tus clientes en instantes------------
""")


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
def eliminar_registro(datos):
    id_buscado = input("Ingrese el ID del registro a eliminar: ").upper()#pasa a mayuscula 

    for i in range(len(datos)):
        if datos[i][0] == id_buscado:
            datos.pop(i)
            print("Registro eliminado correctamente.")
            return
    print("No existe un registro con ese ID.")
    
#bucle principal del programa
while True:
    print("\n=================================================")
    print("               MENÚ PRINCIPAL")
    print("=================================================")
    print("1. Imprimir informe completo de compromiso")
    print("2. Agregar datos al registro de duración y clics")
    print("3. Eliminar datos del registro por ID")
    print("4. Imprimir informe por ID")
    print("-------------------------------------------------")

    intentos = 0
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-4): "))

            if 1 <= opcion <= 4:
                break
            else:
                print("Error: Debe ingresar un número entre 1 y 4.")
                intentos += 1

        except ValueError:
            print("Error: Debe ingresar únicamente un número Entero.")
            intentos += 1

        if intentos == 3:
            print("\nHa agotado los 3 intentos. Se mostrará nuevamente el menú.\n")
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
                     print("La duración no puede ser negativa.")
            except ValueError:
                print("Debe ingresar un número entero.")
        # Entrada de numero de clics
        while True:
            try:
                 clics = int(input("Ingrese la cantidad de clics: "))
                 if clics >= 0:
                   break
                 else:
                   print("Los clics no pueden ser negativos.")
            except ValueError:
                    print("Debe ingresar un número entero.")
        #agrega nuevo registro al final de la matriz
        agregar_registro(datos)
    elif opcion == 3:
        eliminar_registro(datos)
    elif opcion == 4:
        print("prueba 4")
    