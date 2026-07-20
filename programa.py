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
    
    