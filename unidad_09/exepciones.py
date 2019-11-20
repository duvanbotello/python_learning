while True:
    try:
        n = float(input("Intruducce un numero: "))
        print(n+5)
        
    except:
        print('Ocurrio un error al digitar los datos.')
    else:
        print('Todo funciona correctamente')
        break
    finally:
        print('fin de la ejecucion')


