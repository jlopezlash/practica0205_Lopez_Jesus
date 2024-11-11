#Escribir una función que reciba un número entero positivo y devuelva su factorial.
#Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))