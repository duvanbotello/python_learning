class Galletas:
    chocolate = True
    sabor = None
    color = None
    forma = "Cuadrado"

    def __init__(self):
        print("Se creo una Galleta")

    def __del__(self):
        print("se esta eliminando la pelicula")
    
    def chocolatear(self):
        self.chocolate = True



galleta = Galletas()

print(galleta.forma)