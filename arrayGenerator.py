import random

def arrayGenerator():
    tamanho = random.randint(1, 100)
    array = []
    for i in range(tamanho):
        array.append(random.randint(0, 100))
    return array

def getInvCount(arr, n):
  
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
  
    return inv_count

print('Qual o nivel de desordenacao voce gostaria: ')
  
# Driver Code
arr = arrayGenerator()
n = len(arr)
print("Number of inversions are",
              getInvCount(arr, n))

print(arrayGenerator())