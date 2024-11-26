from random import randint

# OBS: o min_index caminha até encontrar o menor valor de todo o array
def selection_sort(arr):
    
    for i in range(len(arr)-1): # O indice i precisa chegar até o penultimo indice da lista 
        min_index = i  # Pega, primeiramente, o valor i, ou seja, o primeiro valor 
        maior_index = 0
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]: #verifica se o valor arr[j] é menor do que o valor do arr[min_index]
                min_index = j # caso o arr[j] seja menor do que arr[min_index]. O min_index passa a ser o indice j 
            else:
                maior_index = j

        #caso não encontre um valor menor do que o min_index, passa para essa segunda parte
        if min_index != i: #aqui é feito a troca desses dois índices
            temp = arr[i]
            arr[i] = arr[min_index] # menor valor vai para o indice i
            arr[min_index] = temp 
            
    return arr

arr = [0] * 10
for i in range(len(arr)):
    arr[i] = randint(1, 20)


print("Lista desordenada:", arr)
print("Lista ordenada", selection_sort(arr))

"""
[8,7,5,2,3]
i= 8
min_index = 2

[2, 7, 5, 8, 3]
"""