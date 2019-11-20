class Producto:
    def __init__(self,codigo,nombre,precio,descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    
    def __str__(self):
        return f"Codigo\t\t{self.codigo}\n"\
               f"Nombre\t\t{self.nombre}\n"\
               f"Precio\t\t{self.precio}\n"\
               f"Descripcion\t{self.descripcion}\n"\


class Adorno(Producto):
    pass


adorno = Adorno("20554", "Vaso adornado", 15, "Vaso de procelana")

print(adorno)