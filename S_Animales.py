class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

class Perro(Animal):
    def __init__(self, nombre, edad, sonido):
        super().__init__(nombre, edad)
        self.sonido = sonido

    def hacerSonido(self):
        return f"{self.nombre} con {self.edad} años de edad, esta diciendo {self.sonido}"
    
class Pajaro(Animal):
    def __init__(self, nombre, edad, sonido):
        super().__init__(nombre, edad)
        self.sonido = sonido
    
    def hacerSonido(self):
        return f"{self.nombre} con {self.edad} años de edad, esta diciendo {self.sonido}"
        

class Gato(Animal):
    def __init__(self, nombre, edad, sonido):
        super().__init__(nombre, edad)
        self.sonido = sonido

    def hacerSonido(self):
        return f"{self.nombre} con {self.edad} años de edad, esta diciendo {self.sonido}"
    
animal1 = Perro("Tomy", 5, "¡Guau Guau!")
print(animal1.hacerSonido())

animal2 = Gato("Kite", 2, "¡Miaaaaaaaau!")
print(animal2.hacerSonido())

animal3 = Pajaro("Piolin", 2, "Pio Pio")
print(animal3.hacerSonido())