from gpiozero import PWMLED
from time import sleep

servo = PWMLED(12, frequency=50)

def mover_servo(angulo):
    if 0 <= angulo <= 180:
        servo.value = (angulo / 1800.0) + 0.025
        sleep(0.5)
        print("Angulo")
        servo.off()
    else:
        print("El ángulo debe estar entre 0 y 180 grados.")

# Ejemplo de uso
if __name__ == '__main__':
    try:
        while True:
            angulo = int(input("Ingrese el ángulo (0 a 180 grados): "))
            mover_servo(angulo)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")