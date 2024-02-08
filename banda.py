from gpiozero import PWMOutputDevice
from gpiozero import Button
import time
import threading
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
import servo

# Configuración de pines
pin_derecha = PWMOutputDevice(23)
pin_izquierda = PWMOutputDevice(24)
pin_entrada_sensor = Button(21)



pin_derecha.value = 0
pin_izquierda.value = 25 / 100.0
caja1 = None
caja2 = None
caja3 = None
caja4 = None

app = Flask(__name__)

ngrok_address = "http://3fda-200-69-103-254.ngrok-free.app"

@app.route('/')
def index():
    return render_template('index.html', ngrok_address=ngrok_address)


@app.route('/controlar_banda', methods=['POST'])
def controlar_banda():
    global caja1, caja2, caja3, caja4
    if request.method == 'POST':
        caja1 = request.form.get('select1')#0
        caja2 = request.form.get('select2')#90
        caja3 = request.form.get('select3')#180
        print(caja1)
        print(caja2)
        print(caja3)
    return redirect(url_for('index'))
           
        
        
def tomar_foto():
    # Capturar imagen desde la cámara
    camara = cv2.VideoCapture(0)
    ret, imagen = camara.read()
    camara.release()
    
    if ret:
        # Convertir imagen a formato RGB
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
        # Realizar la detección de color
        color = detectar_color(imagen_rgb)
        ###
        if color == caja1:
            servo.mover_servo(0)
        if color == caja2:
            servo.mover_servo(90)
        if color == caja3:
            servo.mover_servo(180)
        else:
            pass
            
        
        print("Color detectado:", color)
        
    else:
        print("No se pudo capturar la imagen")

def detectar_color(imagen):
    # Definir los rangos de color para cada color (rojo, verde, azul)
    rango_rojo = ([0, 100, 100], [20, 255, 255])
    rango_verde = ([36, 100, 25], [70, 255, 255])
    rango_azul = ([90, 100, 50], [150, 255, 255])


    
    # Aplicar las máscaras de color
    mascara_rojo = aplicar_mascara(imagen, rango_rojo)
    mascara_verde = aplicar_mascara(imagen, rango_verde)
    mascara_azul = aplicar_mascara(imagen, rango_azul)
    
    # Contar los píxeles blancos en cada máscara
    num_pixeles_rojos = np.sum(mascara_rojo == 255)
    num_pixeles_verdes = np.sum(mascara_verde == 255)
    num_pixeles_azules = np.sum(mascara_azul == 255)
    
    # Determinar el color predominante
    color = None
    max_pixeles = max(num_pixeles_rojos, num_pixeles_verdes, num_pixeles_azules)
    if max_pixeles == num_pixeles_rojos:
        color = "Rojo"
    elif max_pixeles == num_pixeles_verdes:
        color = "Verde"
    elif max_pixeles == num_pixeles_azules:
        color = "Azul"
    
    return color

def aplicar_mascara(imagen, rango_color):
    # Convertir imagen a formato HSV
    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_RGB2HSV)
    
    # Definir los límites inferior y superior de la máscara de color
    lower = np.array(rango_color[0], dtype=np.uint8)
    upper = np.array(rango_color[1], dtype=np.uint8)
    
    # Aplicar la máscara
    mascara = cv2.inRange(imagen_hsv, lower, upper)
    
    return mascara



def moviendo_banda():
    while True:
        if pin_entrada_sensor.is_pressed:
            print("Caja Detectada")
            tomar_foto()
            time.sleep(1.5)
    

mi_hilo = threading.Thread(target=moviendo_banda)
mi_hilo.start()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)     
