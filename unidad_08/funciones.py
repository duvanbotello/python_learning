def saludar():
    print('Hola curso pyhton')


saludar()

def test():
    global n
    n=10
    print(n)

n = 5
print(n)
test()

#retornando valores

def saludar2():
    return "Retornando valores"

print(saludar2())

#recibiendo parametros y retornando valores

def suma(a,b):
    return a + b

print(suma(2,2))


#argumentos y parametros

f = suma(b = 2, a = 5)
print(f)