# Etapas:
# 1- fazer o merge reponsavel por unir os dois arrays ja ordenados
# 2- fazer os algoritmos de ordenacao, ou seja, separar o array e fazer a ordenacao utilizando de alguns algoritmos de ordenacao nao so o mergesort
# 3- Contar o numero de inversoes realizadas, responsavel por identificar o nivel de sortness daquele Array, deve ser feito em cada algoritmo de ordenacao, acredito que seja o mesmo para todos

def bubbleSort(array, l, r):
    i = l
    j = l
    for i in range(r):
        for j in range(r):
            if(array[j+1] < array[j]):
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp 

def insertionSort(array, l, r):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    
def selectionSort(array, l, r):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if(array[j] < array[minimum]):
                minimum = j
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

def merge(array, l, m, r):

    R = [0]*len(array) # mudar
    i = l
    j = m + 1
    k = 0
    inversoes = 0

    while i <= m and j <= r:
        if array[i] <= array[j]:
            R[k] = array[i]
            k += 1
            i += 1
        else:
            R[k] = array[j]
            inversoes += (m-i + 1)
            k += 1
            j += 1

    while i <= m:
        R[k] = array[i]
        k += 1
        i += 1 

    while j <= r:
        R[k] = array[j]
        k += 1
        j += 1 

    k=0
    for loop in range(l, r + 1):
        array[loop] = R[loop]

    return inversoes


array = [7, 3, 2, 5, 4, 3]
insertionSort(array, 0, len(array) - 1)
print(array)