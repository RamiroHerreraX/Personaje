from machine import Pin, PWM
from time import sleep_us, sleep
from hcsr04 import HCSR04
import _thread

# Pin de LED's 
ledPin = Pin(4, Pin.OUT)
# Declaro servo
servo = PWM(Pin(19), freq = 50)

# Crear el objeto buzzer
buzzer = PWM(Pin(12), freq=100, duty=512)

# Declaramos el objeto sensor
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=24000)
count = 0

# Declaro los pines del stepper motor
IN1 = Pin(26,Pin.OUT)
IN2 = Pin(25,Pin.OUT)
IN3 = Pin(33,Pin.OUT)
IN4 = Pin(32,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

# Función para controlar el motor a pasos
def control_motor():
    while True:
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
                sleep(0.001)
                

# Iniciar el hilo para controlar el motor a pasos
_thread.start_new_thread(control_motor, ())

# Declaración de una función para emitir sonidos
def sonido(frecuencia, duracion):
    buzzer.freq(frecuencia)
    buzzer.duty(512)
    sleep(duracion)
    buzzer.duty(0)  # Apagar el buzzer al final de la duración



# Melodía de "Jingle Bells" con frecuencias y duraciones aproximadas
melodia_jingle_bells = [ 
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (330, 1.0),  # Mi
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (330, 1.0),  # Mi
    (330, 0.5),  # Mi
    (392, 0.5),  # Sol
    (262, 1.0),  # Do
    (294, 0.5),  # Re
    (294, 0.5),  # Re
    (262, 1.0),  # Do
    (392, 0.5),  # Sol
    (330, 1.5),  # Mi 
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (392, 0.5),  # Sol
    (262, 1.0),  # Do
    (294, 0.5),  # Re
    (294, 0.5),  # Re
    (262, 1.0),  # Do
    (392, 0.5),  # Sol
    (330, 1.5)   # Mi
]

# Nueva melodía para "We Wish You a Merry Christmas"
melodia_wish_you_merry_christmas = [
    (392, 0.5),  # Sol
    (392, 0.5),  # Sol
    (440, 0.5),  # La
    (392, 0.5),  # Sol
    (349, 0.5),  # Fa
    (330, 1.0),  # Mi
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (330, 0.5),  # Mi
    (349, 0.5),  # Fa
    (392, 1.0),  # Sol
    (392, 0.5),  # Sol
    (392, 0.5),  # Sol
    (392, 0.5),  # Sol
    (440, 0.5),  # La
    (392, 0.5),  # Sol
    (349, 0.5),  # Fa
    (330, 1.0),  # Mi
    (294, 0.5),  # Re
    (294, 0.5),  # Re
    (330, 0.5),  # Mi
    (349, 0.5),  # Fa
    (392, 1.0),  # Sol
    (392, 0.5),  # Sol
    (392, 0.5),  # Sol
    (392, 0.5),  # Sol
    (440, 0.5),  # La
    (392, 0.5),  # Sol
    (349, 0.5),  # Fa
    (330, 1.0),  # Mi
    (294, 0.5),  # Re
    (294, 0.5),  # Re
    (262, 2.0),  # Do
]


# Variables para controlar la alternancia de melodías
current_melody = melodia_jingle_bells  # Comenzar con la melodía "Jingle Bells"
alternate = False  # Variable para alternar entre melodías


while True:
    
    # Declaramos variable para almacenar la distancia
    
    sleep(1)
    servo.duty(75)
    sleep(1)
    servo.duty(125)
    sleep(1) 
    servo.duty(75)
    sleep(1)
    
    distancia = sensor.distance_cm()
    print("Distancia: ", distancia, " cm.")
    
    # Resto de la lógica principal
    if distancia <= 30: 
        if alternate:
            current_melody = melodia_wish_you_merry_christmas
        else:
            current_melody = melodia_jingle_bells
        alternate = not alternate  # Cambiar entre melodías
    
        for nota in current_melody:
            sonido(nota[0], nota[1])
            sleep(0.1)  # Pausa de 0.1 segundos entre notas para una mejor separación
             # Nuevos valores para el servo
            if count % 2 == 0:
                    ledPin.value(0)
            else:
                    ledPin.value(1)
            count += 1
    else:
        sonido(5, 0.1)  # Una frecuencia de ejemplo (5) y duración corta si la distancia es menor a 30 cm
    sleep(1)




