datos = [
    ["AAA001", 210, 12],
    ["AAA002", 45, 5],
    ["AAA003", 120, 6],
    ["AAA004", 200, 2],
    ["AAA005", 150, 7]
]

#funcion para calcular el compromiso de los clientes:
def calcular_compromiso (duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"
    
    