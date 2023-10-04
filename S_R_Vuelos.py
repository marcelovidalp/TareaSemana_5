class Reserva:
    def __init__(self, nombre_pasajero, numero_vuelo, fecha):
        self.nombre_pasajero = nombre_pasajero
        self.numero_vuelo = numero_vuelo
        self.fecha = fecha

    def mostrarDetalle(self):
        print(f"Nombre del Pasajero: {self.nombre_pasajero}")
        print(f"Numero del Vuelo: {self.numero_vuelo}")
        print(f"Fecha del Vuelo: {self.fecha}")

class ReservaEconomica(Reserva):
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, asientos_asig):
        super().__init__(nombre_pasajero, numero_vuelo, fecha)
        self.asientos_asig = asientos_asig

    def mostrarDetalle(self):
        super().mostrarDetalle()
        print(f"Asientos Asignados: {self.asientos_asig}")

class ReservaBussines(Reserva):
    def __init__(self, nombre_pasajero, numero_vuelo, fecha, vip_acceso):
        super().__init__(nombre_pasajero, numero_vuelo, fecha)
        self.vip_acceso = vip_acceso

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
    reserva_eco = ReservaEconomica("Benjamin Gallardo", "V23", "10/10/2023", ["C2", "C3"])
    reserva_bussines = ReservaBussines("Marcelo Gonzales", "V34", "20/10/2023", True)
    reservaFClass = ReservaPrimeraClase("Juanita Aguirre", "V32", "12/10/2023", "Mayordomo Personal")

    print("Detalles de la Reserva Economica:")
    reserva_eco.mostrarDetalle()

    print("------------------------------------------")

    print("Detalles de la Reserva Bussines:")
    reserva_bussines.mostrarDetalle()
    print(reserva_bussines.verificar_vip())

    print("------------------------------------------")

    print("Detalles de la Reserva de Primera Clase:")
    reservaFClass.mostrarDetalle()





