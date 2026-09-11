import threading
import time

buffer = []
capacidad = 3
condicion = threading.Condition()


def productor():
    for producto in range(1, 6):

        with condicion:
            while len(buffer) == capacidad:
                print("Buffer lleno. Productor esperando...")
                condicion.wait()

            buffer.append(producto)
            print(f"Productor produjo: {producto}")
            condicion.notify_all()
        time.sleep(0.5)

def consumidor():
    for _ in range(1, 6):
        with condicion:
            while len(buffer) == 0:
                print("Buffer vacío. Consumidor esperando...")
                condicion.wait()

            producto = buffer.pop(0)
            print(f"Consumidor consumió: {producto}")
            condicion.notify_all()
        time.sleep(2.5)

def ejecutar_demo_monitor():

    hilo_productor = threading.Thread(target=productor)
    hilo_consumidor = threading.Thread(target=consumidor)

    hilo_productor.start()
    hilo_consumidor.start()

    hilo_productor.join()
    hilo_consumidor.join()

    print("Demostración de monitor finalizada.")


if __name__ == "__main__":
    ejecutar_demo_monitor()
