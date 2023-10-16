class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def cal_salario_anual(self):
        return self.salario * 12
    
    def describir_rol(self):
        return f"Soy {self.nombre}, y tengo {self.edad} años. \n Salario: {self.salario}"

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, tipo):
        super().__init__(nombre, edad, salario)
        self.tipo = tipo
        self.subordinados = []

    def asig_subordinados(self, subordinado):
        self.subordinados.append(subordinado)
        print(f"{subordinado.nombre} ha sido asignado a {self.nombre}\n")

    def listar_subordinados(self):
        print(f"Lista de subordinados de {self.nombre}")
        for subordinado in self.subordinados:
            print(subordinado.nombre)

    def describir_rol(self):
        return f"Soy {self.nombre} y tengo {self.edad} años. \n Salario: {self.salario}"

class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, rubro):
        super().__init__(nombre, edad, salario)
        self.rubro = rubro
        self.lista_ing = [] 

    def asign_proyecto(self, proyecto):
        self.proyecto_asign = proyecto
        print(f"Ha sido asignado el proyecto {proyecto}")

    def listar_proyecto(self):
        if self.proyecto_asign:
            return f"Estoy trabajando el el proyecto {self.proyecto_asign}"
        else:
            return "No tengo proyecto asignado por el momento."

    def describir_rol(self):
        return f"Soy el {self.rubro}, me llamo {self.nombre} y tengo {self.edad} años. \n Salario: {self.salario}"

class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, tipo):
        super().__init__(nombre, edad, salario)
        self.tipo = tipo

    def reuniones(self):
        print(f"Estoy organizando una reunion para el {self.tipo} {self.nombre}")

    def agenda(self):
        print(f"Estoy gestionando la agenda del {self.tipo} {self.nombre}")

    def describir_rol(self):
        return f"Soy el {self.tipo}, me llamo {self.nombre} y tengo {self.edad} años. \n Salario: {self.salario}"
    

empleado1 = Empleado("Eliana", 34, 46000)
gerente1 = Gerente("Jorge", 28, 50000, "Gerente de Produccion")
ingeniero1 = Ingeniero("Santiago", 27, 32000, "Desarrollador Web")
asistente1 = Asistente("Juanita", 34, 10000, "Asistente Ejecutiva")

gerente1.asig_subordinados(ingeniero1)
gerente1.asig_subordinados(asistente1)

ingeniero1.asign_proyecto("Sistema Gestion de Proyectos")

print(empleado1.describir_rol())
print(gerente1.describir_rol())
print(ingeniero1.describir_rol())
print(asistente1.describir_rol())

print(f"El salario de {empleado1.nombre} es {empleado1.cal_salario_anual}")

gerente1.listar_subordinados()


    


        
