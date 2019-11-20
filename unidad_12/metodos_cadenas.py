#caracteres en mayuscula
print("Hola mundo".upper())

#caracteres en minuscula
print("Hola mundo".lower())

#primer caracter en en mayuscula
print("Hola mundo".capitalize())

#el primer caracter de cada palabra en mayuscula
print("Hola mundo".title())

#cuenta cuantas veces aparece una subcadena en la cadena
print("Hola mundo mundo".count("mundo"))

#devuelve el indece donde aparece la cadena -1 si no hay nada por el inicio
print("Hola mundo".find("mundo"))

#devuelve el indece donde aparece la cadena -1 si no hay nada por el final
print("Hola mundo".rfind("mundo"))

#devuelve true si una cadena es solo numeros
print("123".isdigit())

#devuelve true si una cadena es solo letras
print("123".isalpha())

#devuelve true si una cadena es solo minusculas
print("asdasd".islower())

#devuelve una lista con elementos que esta separados por espacios
print("123 hola como estas".split(" "))

#remplaza una subcadena por tra
print("Hola mundo".replace('o','0'))