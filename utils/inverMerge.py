def inverMerge(vetor, aux, esquerda, meio, direita) -> int:
    """
    Combina dois vetores ordenados em um único vetor (também ordenado).
    """
    
    totalInver = 0

    countEsquerda = esquerda
    countMeio = meio + 1
    sortedArray = esquerda

    while countEsquerda <= meio and countMeio <= direita:
        
        if vetor[countEsquerda] <= vetor[countMeio]:
            aux[sortedArray] = vetor[countEsquerda]

            sortedArray += 1
            countEsquerda += 1

        else:
            aux[sortedArray] = vetor[countMeio]

            totalInver  += (meio - countEsquerda) + 1

            sortedArray += 1
            countMeio   += 1

    while countEsquerda <= meio:
        aux[sortedArray] = vetor[countEsquerda]
        sortedArray += 1
        countEsquerda += 1

    while countMeio <= direita:
        sortedArray += 1
        countMeio   += 1

    return totalInver

def inverMergesort(vetor, aux, esquerda, direita) -> int:

    totalInver = 0

    if direita <= esquerda:
        return 0

    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    totalInver += inverMergesort(vetor, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    totalInver += inverMergesort(vetor, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    totalInver += inverMerge(vetor, aux, esquerda, meio, direita)

    return totalInver

def inversoes(vetor: list, tamanho: int) -> int:
    auxArry = [0] * tamanho
    return inverMergesort(vetor, auxArry, 0, tamanho - 1)
