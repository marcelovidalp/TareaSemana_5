class Reserva:                                                                              #genero la clase de reserva (CLASE PADRE)
    def __init__(self, nombre_pasajero, numero_vuelo, fecha):                               #metodo constructor para darle atributos al objeto
        self.nombre_pasajero = nombre_pasajero                                              #defenimos el atributo del nombre del pasajero
        self.numero_vuelo = numero_vuelo                                                    #defenimos el atributo del numero de vuelo
        self.fecha = fecha                                                                  #defenimos el atributo de fecha del vuelo

    def mostrarDetalle(self):                                                               #genero el metodo de mostrar detalle
        print(f"Nombre del Pasajero: {self.nombre_pasajero}")                               #se imprime el nombre del pasajero
        print(f"Numero del Vuelo: {self.numero_vuelo}")                                     #se imprime el numero del vuelo
        print(f"Fecha del Vuelo: {self.fecha}")                                             #se imprime la fecha del vuelo

class ReservaEconomica(Reserva):                                                            #Genero la clase Reserva economica (SUBCLASE DE LA CLASE RESERVA)
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, asientos_asig):                #Metodo constructor del objeto, con sus respectivos atributos
        super().__init__(nombre_pasajero, numero_vuelo, fecha)                              #con el super() invocamos los atributos de la clase padre
        self.asientos_asig = asientos_asig                                                  #definimos los asientos asignados

    def mostrarDetalle(self):                                                               #Genero el metodo mostrar detalle
        super().mostrarDetalle()                                                            #invoco el codigo del metodo mostrarDetalle desde la clase padre
        print(f"Asientos Asignados: {self.asientos_asig}")                                  #hacemos que imprima el atributo adicional, imprime los asientos asignados

class ReservaBussines(Reserva):                                                             #Generamos la clase de Reserva Bussines (SUBCLASE DE LA CLASE RESERVA)
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, vip_acceso):                   #Le entregamos los atributos con el metodo constructor
        super().__init__(nombre_pasajero, numero_vuelo, fecha)                              #Invocamos los atributos definidos desde la clase padre
        self.vip_acceso = vip_acceso                                                        #definimos el atributo de vip_acceso (para saber si el pasajero cuenta o no con VIP)

    def verificar_vip(self):                                                                 
        if self.vip_acceso == True:
            return "\nEl pasajero tiene acceso a la sala VIP."
        else: 
            return "\nEl pasajero no tiene acceso a la sala VIP."

    def mostrarDetalle(self):
        super().mostrarDetalle()
        print(f"Acceso VIP: {self.vip_acceso}")

class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, servicio_especial):          #mayordomo u otros
        super().__init__(nombre_pasajero, numero_vuelo, fecha)
        self.servicio_especial = servicio_especial

    def mostrarDetalle(self):
        super().mostrarDetalle()
        print(f"Servicio Especial a Bordo: {self.servicio_especial}")

if __name__ == "__main__":
    reserva_eco = ReservaEconomica("Benjamin Gallardo", "V23", "10/10/2023", ["C2", "C3"])                 #<- Instancia de la Reserva Economica
    reserva_bussines = ReservaBussines("Marcelo Gonzales", "V34", "20/10/2023", True)                      #<- Instancia de la Reserva Bussines
    reservaFClass = ReservaPrimeraClase("Juanita Aguirre", "V32", "12/10/2023", "Mayordomo Personal")      #<- Instancia de la Reserva de Primera Clase

    print("Detalles de la Reserva Economica:")                                                             
    reserva_eco.mostrarDetalle()                                                                           #<- LLamo al metodo mostrarDetalle de la clase de
                                                                                                           # reserva economica
    print("------------------------------------------")                                                    #<- para separar los tipos de reserva

    print("Detalles de la Reserva Bussines:")                                                              
    reserva_bussines.mostrarDetalle()                                                               #<- LLamo al metodo mostrarDetalle de la clase reserva bussines
    print(reserva_bussines.verificar_vip())                                                         #<- llamo al metodo verificac vip de la clase reserva bussines

    print("------------------------------------------")                                             #<- para separar los tipos de reserva

    print("Detalles de la Reserva de Primera Clase:")
    reservaFClass.mostrarDetalle()                                                                  #<- LLamo al metodo mostrarDetalle de la clase reserva de primera clase





