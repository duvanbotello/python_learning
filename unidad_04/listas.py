#Definiendo una lista

numeros = [1,2,3,4]
datos = ["hola",2,"como estas",3]

print(numeros)
print(datos)

#mostramos datos de la lista por indice
print(datos[0])

#mostramos datos de lista por Slicing
print(datos[0:3])

#funcion de listas

c = len(datos) 
datos.append(12)
print(c)
print(datos)