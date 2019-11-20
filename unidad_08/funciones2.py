#argumentos indefinidos

def ejemplo(*args):
    for dato in args:
        print(dato)

ejemplo(1,2,3,4)

def ejemplo2(**kwargs):
    print(kwargs)

ejemplo2(a=2, b='hola', c=5)