# Juego de Piedra, Papel o Tijera con Detección de Manos

Este es un pequeño juego de piedra, papel o tijera implementado en Python utilizando las librerías OpenCV y MediaPipe para la detección de manos. El juego permite jugar contra la computadora usando gestos de las manos para elegir piedra, papel o tijera.

## Requisitos

- Python 3.x
- OpenCV
- MediaPipe
- numpy

## Instalación

Se recomienda crear un entorno virtual para instalar las dependencias necesarias. Para ello, sigue los siguientes pasos:

1. Clona este repositorio:

    ```sh
    git clone https://github.com/brianrscode/piedra-papel-tijera-opencv.git
    cd piedra-papel-tijera-opencv
    ```

2. Crea un entorno virtual:

    ```sh
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:

        ```sh
        venv\Scripts\activate
        ```

    - En macOS y Linux:

        ```sh
        source venv/bin/activate
        ```

4. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script principal:

    ```sh
    python main.py
    ```

2. Coloca tu mano derecha frente a la cámara y realiza los siguientes gestos:

    - **Iniciar juego**: Pulgar, índice y meñique levantados.
    - **Piedra**: Todos los dedos cerrados.
    - **Papel**: Todos los dedos abiertos.
    - **Tijera**: Solo el índice y el medio levantados.

3. El juego comenzará y la computadora hará una selección aleatoria. Dependiendo del resultado, se mostrará una imagen indicando si ganaste, perdiste o empataste.

4. Para salir del juego, presiona la tecla `q`.

## Estructura del Proyecto

- `main.py`: Script principal del juego.
- `HandsDetector.py`: Clase personalizada para la detección de manos utilizando MediaPipe.
- `imgs/`: Carpeta que contiene las imágenes utilizadas en el juego (inicio, elección, ganado, perdido, empate).

## Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o enviar un pull request.
