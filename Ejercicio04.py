#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(N):
    '''Calcular la media de unos numeors
    Para esto necesitare unos numeros y su longitud'''
    m = sum(N) / len(N)
    return m
print (media([4, 5, 7, 9, 1, 3]))