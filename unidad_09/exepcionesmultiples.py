while True:
    try:
        n = float(input("Introducce numero: "))
        print(5/n)
    except ValueError:
        print("Por favor intruducce un numero")
    except ZeroDivisionError:
        print("Inserte un numero mayor a 0")
    except Exception as e: #Guardamos el typo de error
        print("Ha ocurrido un error =>", type(e).__name__)