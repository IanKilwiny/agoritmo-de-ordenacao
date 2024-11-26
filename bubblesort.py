def bubbleSort(arr):
    trocou = False
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                trocou = True
    
        if not trocou:
            break
    
    return arr

arr = [1,9,4,2,6,3,25]

print("Desordenado:", arr)
print("Ordenado: ",bubbleSort(arr))