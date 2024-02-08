
# Sistema de Clasificación de Objetos por Color con Control de Banda y de un Brazo Robotico
Este repositorio contiene un proyecto de Python que utiliza una Raspberry Pi y una cámara para clasificar objetos con un brazo robotico, según su color. La aplicación se basa en la detección de color mediante la biblioteca OpenCV y utiliza GPIO para el control de servo motores que constituyen el brazo robotico, adicionalmete esta conectada una banda transportadora en movimiento con un motoreductor. Adicionalmente se emplea un sensor infrarojo con modulo digital para que al tomar un pulso digital se active la camara para el proceso de detección de color.

El funcionamiento o seleccion de la ubicacion para clasificar los objetos se determinan a partir de una conexión usando la raspberry pi como servidor mediante una configuración con ngrok. El usuario selecciona segun tres posiciones los colores que van en cada aposición 
¡Claro! Aquí está la versión actualizada de la descripción que incluye la información sobre el uso de ngrok para configurar las posiciones de la banda transportadora:



## Características destacadas:

- **Detección de Color:** Utiliza la cámara para detectar objetos de diferentes colores (rojo, verde, azul) en una banda transportadora.
- **Control de Banda:** Ajusta la velocidad de la banda transportadora según el color detectado utilizando moto reductor.
-**Brazo Robotico:** El brazo robotico esta constituido por cuatro servo motores que ajustaran su posicion a las coordenadas indicads por el usuario cada que se detecte un objeto en el final de la banda. 
- **Interfaz Web:** Proporciona una interfaz web a través de Flask para el control manual y la visualización de la detección de color.
- **Configuración Dinámica:** Permite configurar los ángulos de giro del servo motor para cada color a través de la interfaz web.
- **Uso con ngrok:** La interfaz web es accesible a través de ngrok, lo que permite al usuario configurar las posiciones de la banda transportadora de forma remota.

## Estructura del Proyecto:

- **Código Principal:** El código principal se encuentra en un solo archivo (`app.py`) que utiliza las bibliotecas gpiozero, Flask y OpenCV. Tambien se importa el archivo (`servo.py`) para usar las funcionalidades configuradas en ese mismo archivo, el cual determina el movimiento del brazo robotico.
- **Módulo de Servo:** La funcionalidad del servo motor se encapsula en el módulo `servo.py`.
- **Interfaz Web:** Utiliza Flask para crear una interfaz web simple y fácil de usar.

## Instrucciones de Uso:

1. **Configuración de Pines:** Configura los pines de la Raspberry Pi para el control de la banda y el sensor.
2. **Ejecución del Proyecto:** Ejecuta el script `app.py` y accede a la interfaz web desde cualquier navegador.
3. **Uso con ngrok:** Utiliza ngrok para hacer que la interfaz web sea accesible de forma remota y configura las posiciones de la banda transportadora según sea necesario.
4. **Control Manual:** Utiliza la interfaz web para controlar manualmente la banda y configurar los ángulos del servo para cada color.
5. **Detección Automática:** La aplicación detecta automáticamente los objetos de color en la banda y ajusta la posición de la banda en consecuencia.

## Requisitos:

- Raspberry Pi con GPIO.
- Cámara compatible con la Raspberry Pi.
- Bibliotecas Python: gpiozero, Flask, OpenCV.

## Contribuciones:

¡Las contribuciones son bienvenidas! Si encuentras mejoras o correcciones, no dudes en enviar pull requests.

## Licencia:

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---
