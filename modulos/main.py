import os

class Playerd:
    def __init__(self, id_Playerd, nombre, edad, categoria):
        self.id_Playerd = id_Playerd
        self.categoria = categoria
        self.nombre = nombre
        self.edad = edad
        self.plus_puntos = 0
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_perdidos = 0        

class TorneoTenis:
    def __init__(self):
        self.categorias = {'Novato': [], 'Intermedio': [], 'Avanzado': []}

    def registroJugador(self, id_Playerd, nombre, edad, categoria):
        Playerd = Playerd(id_Playerd, nombre, edad, categoria)
        if categoria in self.categorias.keys():
            if (categoria == 'Novato' and 15 <= edad <= 16) or \
               (categoria == 'Intermedio' and 17 <= edad <= 20) or \
               (categoria == 'Avanzado' and edad > 20):
                self.categorias[categoria].append(Playerd)
                print(f"{nombre} se registró correctamente en la categoría: {categoria}")
            else:
                print(f"{nombre} es muy joven o viejo para ser novato, intermedio o avanzado")
        else:
            print("No se encuentra la categoría")

    def inicio_PanCamp(self):
        for categoria, Playerdes in self.categorias.items():
            if len(Playerdes) < 5:
                print(f"Faltan Playerdes en la categoría: {categoria} para comenzar")
            else:
                print(f"Comenzó el PanCamp de la categoría: {categoria}")

    def registrar_partido(self, id_ganador, id_perdedor, punt_ganador, punt_perdedor):
        ganador = None
        perdedor = None

        for categoria, Playerdes in self.categorias.items():
            for Playerd in Playerdes:
                if Playerd.id_Playerd == id_ganador:
                    ganador = Playerd
                elif Playerd.id_Playerd == id_perdedor:
                    perdedor = Playerd

        if ganador is not None and perdedor is not None:
            ganador.partidos_jugados += 1
            perdedor.partidos_jugados += 1
            ganador.partidos_ganados += 1
            perdedor.partidos_perdidos += 1
            ganador.plus_puntos += punt_ganador - punt_perdedor
            print("El juego fue registrado correctamente")
        else:
            print("No hay ningún registro de ese Playerd")

    def mostrar_estadisticas(self):
        for categoria, Playerdes in self.categorias.items():
            print(f"Categoría: {categoria} ")
            print("| ID | Playerd | Partidos Jugados | Partidos Ganados | Partidos Perdidos | Puntos a Favor |")
            for Playerd in Playerdes:
                print(f"| {Playerd.id_Playerd} | {Playerd.nombre} | {Playerd.partidos_jugados} | {Playerd.partidos_ganados} | {Playerd.partidos_perdidos} | {Playerd.plus_puntos} |")

    def obtener_ganador_categoria(self, categoria):
        if categoria in self.categorias.keys():
            Playerdes_categoria = self.categorias[categoria]
            if Playerdes_categoria:
                ganador = max(Playerdes_categoria, key=lambda Playerd: Playerd.plus_puntos)
                print(f"Hay un ganador en esta categoría: {categoria}. Es {ganador.nombre} con {ganador.plus_puntos} puntos a favor.")
            else:
                print(f"No hay Playerdes en esta categoría: {categoria}.")
        else:
            print("La categoría no existe")

def registroproducto_manualmente(PanCamp):
    id_Playerd = int(input("Fecha de la venta: "))
    nombre = input("nomre y direccion: ")
    edad = int(input("Ingresa la edad del Playerd: "))
    categoria = input("Ingresa la categoría (Novato/Intermedio/Avanzado): ")
    PanCamp.registroJugador(id_Playerd, nombre, edad, categoria)

def main():
    PanCamp = TorneoTenis()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\t\t  Menú ")
        print("\t  1. Gestion de ventas                          ")
        print("\t  2. Compras                             ")
        print("\t  3. Informes              ")
        print("\t  4..salir                      ")
        print(" ")
        opc = input("Elige una opción dentro de (1-4): ")

        continuar = input("¿Deseas registrar un Playerd? (s/n): ")

        if opc == "1":
            registroproducto_manualmente(PanCamp)
        elif opc == "2":
            PanCamp.inicio_PanCamp()
        elif opc == "3":
            id_ganador = int(input("Ingresa la identificación del Playerd ganador: "))
            id_perdedor = int(input("Ingresa la identificación del Playerd perdedor: "))
            punt_ganador = int(input("Ingresa los puntos a favor del Playerd ganador: "))
            punt_perdedor = int(input("Ingresa los puntos a favor del Playerd perdedor: "))
            PanCamp.registrar_partido(id_ganador, id_perdedor, punt_ganador, punt_perdedor)
        elif opc == "4":
            PanCamp.mostrar_estadisticas()
        elif opc == "5":
            categoria = input("Elige la categoría de la cual quieres ver el ganador: ")
            PanCamp.obtener_ganador_categoria(categoria)
        elif opc == "6":
            print("Terminó el programa.")
            break
        else:
            print("El número que ingresaste no existe. Ingresa un número entre (1-4)")

if __name__ == "__main__":
    main()