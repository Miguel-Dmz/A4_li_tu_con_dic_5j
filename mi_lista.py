print("****EJEMPLO DE LISTA**** \n")
arcoiris=["verde","azul","morado","rosa","amarillo","gris"]
print(arcoiris)
longitud=len(arcoiris)
print("elemento que contiene la lista arcoiris " ,len(arcoiris))
print(f"elemento que contiene la lista arcoiris v2 {longitud} \n")

print("****ACCEDIENDO A UN ELEMENTO**** \n")
print(f"elemento en la posicion 0 es {arcoiris[0]} \n")

print("****AGREGAR UN ELEMENTO A LA LISTA**** \n")
arcoiris.append("negro")
print(arcoiris, "\n")

print("****LISTAR LOS ELEMENTOS DE LA LISTA, CICLO FOR**** \n")
for miguel in arcoiris:
    print(miguel)