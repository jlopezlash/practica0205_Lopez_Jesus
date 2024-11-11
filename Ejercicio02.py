#Escribir una función que reciba un número entero positivo y devuelva su factorial.
#Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
def fact(n):
    '''Hace el factorial de un numero entero positivo'''
    for i in range(n-1):
        n = n * (i+1)
    print(n)
fact(5)