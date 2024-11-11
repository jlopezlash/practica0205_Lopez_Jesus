#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.
lista = [2,4,6,8,1,3,5,7,9]
print(lista)
def cuadrado(N):
    '''
    parametro entrada
        -N en lista
    salida
        -lista al cuadrado
    '''
    for i in range(len(N)):
        N[i] = N[i] ** 2
    return N
print(cuadrado(lista))
    
