def merge(X, inicio, fim):
    if inicio < fim:
        meio = int((inicio + fim) / 2)
        merge(X, inicio, meio)
        merge(X, meio + 1, fim)
        intercalar(X, inicio, meio, fim)

        
        
def intercalar(X, inicio, meio, fim):
    aux = [] 
    i, j = inicio, meio + 1
    poslivre = inicio

    while poslivre < fim + 1:
        if i > meio:
            aux.append(X[j])
            j += 1
        elif j > fim:
            aux.append(X[i])
            i += 1
        elif X[j] < X[i]:
            aux.append(X[j])
            j += 1
        else:
            aux.append(X[i])
            i += 1
            
        poslivre = poslivre + 1

    poslivre = 0
    for i in range(inicio, fim+1):
        X[i] = aux[poslivre]
        poslivre = poslivre + 1

    

n = int(input("Entre com o número de elementos de X: "))

#Criando a lista de 5 elementos a partir da entrada do usuário
X = [int(input("Digite o {0}{1}: ".format(i+1, chr(176)))) for i in range(n)]
print("O vetor de entrada é:  ")
print(X)
merge(X, 0, n-1)
print("O vetor ordenado é: ")
print(X)

