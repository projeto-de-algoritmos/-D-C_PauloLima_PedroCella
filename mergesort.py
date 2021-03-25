def merge(vetor, aux, esquerda, meio, direita):
    """
    Combina dois vetores ordenados em um único vetor (também ordenado).
    """
    for k in range(esquerda, direita + 1):
        aux[k] = vetor[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            vetor[k] = aux[j]
            j += 1
        elif j > direita:
            vetor[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            vetor[k] = aux[j]
            j += 1
        else:
            vetor[k] = aux[i]
            i += 1


def mergesort(vetor, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    mergesort(vetor, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    mergesort(vetor, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    merge(vetor, aux, esquerda, meio, direita)

# def merge(vetor, l, m, r):
#     R = []
#     i = l
#     j = m + 1
#     k = 0

#     while(i <= m and j <= r):
#         if(vetor[i] <= vetor[j]):
#             R[k + 1] = vetor[i + 1]
#         else:
#             R[k + 1] = vetor[j + 1]

#     while(i <= m):
#         R[k + 1] = vetor[i + 1]
#     while(j <= r):
#         R[k + 1] = vetor[j + 1]
#     k = 0
#     for i in r:
#         vetor[i] = R[k + 1]

# def mergesort(vetor, l, r):
#     if (l >= r): 
#         return
#     meio = (l+r)/2
#     mergesort(vetor,l,meio)
#     mergesort(vetor,meio + 1, r)
#     merge(vetor,l,meio,r)



vetor = [7, 3, 2, 5, 4, 3]
print("Arranjo não ordenado: ", vetor)
aux = [0] * len(vetor)
mergesort(vetor, aux, 0, len(vetor) - 1)
print("Arranjo ordenado: ", vetor)