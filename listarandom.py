import random 
lista=[]
#se crea la lista vacia 
for i in range(10):
#el for se utiliza para que se repita el ciclo 10 veces
    lista.append(random.randint(0,10))
print(lista)
for i in range(10):
    if i==3:
        print("-----")
    else:
        print(lista[i])