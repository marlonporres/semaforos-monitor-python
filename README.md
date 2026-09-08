# Semáforos y Monitores en Python

## Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python para demostrar el funcionamiento de dos mecanismos de sincronización utilizados en sistemas operativos: los semáforos y los monitores.

La aplicación incluye dos demostraciones independientes.

### Semáforo

La primera demostración simula un estacionamiento con una cantidad limitada de espacios disponibles.

Varios vehículos intentan ingresar al estacionamiento al mismo tiempo, pero solamente una cantidad determinada puede permanecer dentro simultáneamente. Los vehículos que no encuentran espacio disponible deben esperar hasta que otro vehículo salga y libere un espacio.

Para controlar este acceso se utiliza un semáforo mediante `threading.Semaphore`.

### Monitor

La segunda demostración representa el problema productor-consumidor utilizando un buffer compartido de capacidad limitada.

El productor agrega elementos al buffer mientras exista espacio disponible, mientras que el consumidor retira elementos cuando existen datos para consumir.

Cuando el buffer está lleno, el productor debe esperar. De igual manera, cuando el buffer está vacío, el consumidor debe esperar.

Para implementar este comportamiento se utiliza `threading.Condition`, permitiendo controlar el acceso al recurso compartido y coordinar la espera y notificación entre los hilos.

## Objetivo

El objetivo del proyecto es observar de forma práctica cómo diferentes hilos pueden compartir recursos de manera segura y cómo los mecanismos de sincronización permiten controlar su ejecución concurrente.

## Tecnologías utilizadas

- Python
- `threading.Thread`
- `threading.Semaphore`
- `threading.Condition`

## Ejecución

Para iniciar el programa:

```bash
python main.py
```

El programa mostrará un menú similar al siguiente:

```text
==============================
 SEMÁFOROS Y MONITORES
==============================

1. Demostración de semáforo
2. Demostración de monitor
0. Salir
```

Desde este menú se podrá ejecutar cada demostración de manera independiente.
