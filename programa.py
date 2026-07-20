# Matriz inicial: [ID_Cliente, Duracion_segundos, Clics]
datos = [
    ["AAA001", 210, 12],
    ["AAA002", 45, 5],
    ["AAA003", 120, 6],
    ["AAA004", 200, 2],
    ["AAA005", 150, 7]
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
    if opcion == 1:
        informe_total()
    elif opcion == 2:
        print("prueba 2")
    elif opcion == 3:
        print("prueba 3")
    elif opcion == 4:
        print("prueba 4")