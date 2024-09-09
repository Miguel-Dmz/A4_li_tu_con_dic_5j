print("****EJEMPLO DE TUPLAS**** \n")
canciones=("ALMAS GEMELAS","habibi","girl","tokyo")
y=list(canciones)
print(y)
y[1]="inocente"
canciones= tuple(y)
print(canciones)