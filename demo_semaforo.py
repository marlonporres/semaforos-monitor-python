import threading
import time

# Simula 3 espacios disponibles en el estacionamiento.
espacios = threading.Semaphore(3)


def carro(numero):

    print(f"Carro {numero} intenta entrar")

    espacios.acquire()

    try:
        print(f"Carro {numero} entró al estacionamiento")
        time.sleep(2)
        print(f"Carro {numero} salió del estacionamiento")

    finally:
        espacios.release()


def ejecutar_demo():
    print("\n=== DEMOSTRACIÓN DE SEMÁFORO ===")
    print("Estacionamiento con 3 espacios y 6 carros\n")

    hilos = []

    for i in range(1, 7):
        hilo = threading.Thread(
            target=carro,
            args=(i,)
        )

        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("Todos los carros terminaron.")
    print("\nDemostración finalizada.\n")


if __name__ == "__main__":
    ejecutar_demo()
