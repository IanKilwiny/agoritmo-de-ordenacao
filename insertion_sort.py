def insertion_sort(lista):
    tam = len(lista)
    
    
    for i in range(tam):
        chave = lista[i]
        j = i - 1
        while j >=0  and lista[j] > chave:
            lista[j + 1] = lista[j]
            
            j = j - 1
            
        
        lista[j + 1] = chave
        
    
    return lista


lista = [7, 5, 2, 1, 10, 8, 6, 22, 19]

print(insertion_sort(lista))