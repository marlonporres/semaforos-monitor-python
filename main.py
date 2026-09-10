from demo_semaforo import ejecutar_demo


def main():
    while True:
        print("==============================")
        print(" SEMÁFOROS Y MONITORES")
        print("==============================")
        print("1. Demostración de semáforo")
        print("2. Demostración de monitor")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_demo()

        elif opcion == "2":
            print("Monitor pendiente de implementación")

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida...")


if __name__ == "__main__":
    main()
