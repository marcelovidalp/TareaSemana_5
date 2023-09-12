class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.categoria = "Indefinida"

class Electronico(Producto):
    def __init__(self, nombre, precio, tipo):                  #Tipo industrial o domestico
        super().__init__(nombre, precio)
        self.tipo = tipo
        self.categoria = "Electronico"

    def mostrarDetalle(self):
        print(f"Producto {self.nombre}: \nCategoria: {self.categoria} \nCosto: ${self.precio} \nTipo: {self.tipo}")

class Alimenticio(Producto):
    def __init__(self, nombre, precio, grupoA):                #Grupo alimentos naturales o ultraprocesados
        super().__init__(nombre, precio)
        self.grupoA = grupoA
        self.categoria = "Alimenticio"                                      

    def mostrarDetalle(self):
        print(f"Producto {self.nombre}: \nCategoria: {self.categoria} \nCosto: ${self.precio} \nGrupo alimenticio: {self.grupoA}")

class Vestimenta(Producto):
    def __init__(self, nombre, precio, talla):                   #Zapatillas, poleras, pantalones
        super().__init__(nombre, precio)
        self.talla = talla
        self.categoria = "Vestimenta"

    def mostrarDetalle(self):
        print(f"Producto {self.nombre}: \nCategoria: {self.categoria} \nCosto: ${self.precio} \nTalla: {self.talla}")


producto1 = Alimenticio("Takis", 2000, "Ultraprocesado")
producto1.mostrarDetalle()
print("----------------------------------------")

producto2 = Vestimenta("Polera Polo", 50000, "M")
producto2.mostrarDetalle()
print("-----------------------------------------")

producto3 = Electronico("Taladro Bauker", 30000, "Industrial")
producto3.mostrarDetalle()
