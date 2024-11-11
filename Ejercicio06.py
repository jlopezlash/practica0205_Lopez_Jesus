#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
def Decimal(N):
    '''Función que convierte un número binario en decimal.
    Entrada:
        - N: Binario
    Salida:
        Decimal
    '''
    N = list(N)
    N.reverse()
    Decimal = 0
    for i in range(len(N)):
        Decimal += int(N[i]) * 2 ** i
    return Decimal

def Binario(N):
    '''Función que convierte un número decimal en binario.
    Entrada
        - N: Decimal
    Salida:
        Binario
    '''
    Binario = []
    while N > 0:
        Binario.append(str(N % 2))
        N //= 2
    Binario.reverse()
    return ''.join(Binario)

print(Decimal('1111'))
print(Binario(31))