class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, tipo):
        super().__init__(nombre, edad, salario)
        self.tipo = tipo
        self.lista_gerentes = []

    def anadir_gerente(self):
        if self not in self.lista_gerentes:
            self.lista_gerentes.append(self)
            print(f"Se ha añadidio el gerente {self.nombre}")
            
    def mostrar_gerentes(self):
        for i, gerentes in enumerate(self.lista_gerentes):
            print(f"{i + 1}.- {gerentes}")

    def describir_rol(self):
        return f"Soy el {self.tipo}, me llamo {self.nombre} y tengo {self.edad} años. \n Salario: {self.salario}"

class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, rubro):
        super().__init__(nombre, edad, salario)
        self.rubro = rubro
        self.lista_ing = [] 

    def anadir_ing(self):
        if self not in self.lista_ing:
            self.lista_ing.append(self)
            print(f"Se ha añadido el ingeniero {self.nombre}.")

    def describir_rol(self):
        return f"Soy el {self.rubro}, me llamo {self.nombre} y tengo {self.edad} años. \n Salario: {self.salario}"

class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, tipo):
        super().__init__(nombre, edad, salario)
        self.tipo = tipo

    def describir_rol(self):
        return f"Soy el {self.tipo}, me llamo {self.nombre} y tengo {self.edad} años. \n Salario: {self.salario}"
    
while True:
    print("MENU EMPLEADOS.")
    print("1.- Gerentes.")
    print("2.- Ingenieros.")
    print("3.- Asistentes.")
    print("4.- Salir.")
    opcion = int(input("Seleccione un opción: "))

    if opcion == 1:
        print("a) Añadir gerentes.")
        print("b) Mostrar Gerentes.")
        subopcion = input("Seleccione una ocpion: ")

        if subopcion == "a":
            nuevoGerente = Gerente("Jorge Vidal", 55, 2000000, tipo)

        elif subopcion == "b":
            mostrar_gerentes()

    elif opcion == 2:
        print("a) Añadir Ingenieros.")
        print("b) Mostrar Ingenieros.")
        subopcion2 = input("Seleccione una opcion: ")

        if subopcion2 == "a":
            anadir_ing()

        
