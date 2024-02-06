def pedir_tamaño():
    tam = -1
    while tam <= 0 or (tam & (tam - 1)) != 0:
        tam = int(input("Size of the matrix (must be a power of 2): "))
    return tam

def crear_matriz(tam):
    matriz = [[False]*tam for i in range(tam)]
    return matriz

def llenar_matriz(matriz, tam):

    for i in range(tam):
        for j in range(tam):
            matriz[i][j] = input("Digite cada posición de la matriz (T para True, F para False): ") == 'T'

def imprimir_matriz(matriz, tam):
    for i in range(tam):
        for j in range(tam):
            print('T' if matriz[i][j] else 'F', end=' ')
        print()

def es_Hadamard(matriz, tam):
    for i in range(tam):
        for j in range(i+1, tam):
            if sum(matriz[i][k] == matriz[j][k] for k in range(tam)) != tam // 2:
                return False
    return True

def main():
    tam = pedir_tamaño()
    matriz = crear_matriz(tam)
    llenar_matriz(matriz, tam)
    imprimir_matriz(matriz,tam)
    if es_Hadamard(matriz, tam):
        print("La matriz ingresada es una matriz de Hadamard.")
    else:
        print("La matriz ingresada no es una matriz de Hadamard.")

main()
