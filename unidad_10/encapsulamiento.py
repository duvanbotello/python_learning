class Galleta:
    __atributo__privado = "Soy un atributo privado"

 
    def __metodo__privado(self):
        print('Soy un metodo privado')
    
    def atributo_publico(self):
        return self.__atributo__privado
    
    def metodo_publico(self):
        return self.__metodo__privado

    def set_atributo_privado(self,valor):
        self.__atributo__privado = valor
    



galleta = Galleta()

print(galleta.atributo_metodo())
galleta.set_atributo_privado("Cambie")
print(galleta.atributo_publico())