#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def área(Radio):
    '''Calcula el área de un circulo
    Parámetros:
        -Pi
        -Radio^2
    '''
    A = 3.14 * (Radio ** 2)
    return A
print(área(3))
def volumen(altura):
    '''Calcular el volumen de un cilindro
        Se usara el área del circulo anterior y una altura
    '''
    area = área(3)
    V = area * altura
    return V
print(volumen(4))