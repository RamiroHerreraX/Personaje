import network
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
 
# Pin de LED's 
PinA = Pin(16, Pin.OUT)
PinA2 = Pin(13, Pin.OUT)

# Configuración MQTT
MQTT_BROKER = "192.168.1.100"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""  # Asigna un ID de cliente único
MQTT_TOPIC = "pastor/fogata"
MQTT_PORT = 1883

def wifi_connect():
    print("Conectando a la red Wi-Fi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("linksys ", "")  # Cambia esto por tu SSID y contraseña
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print(" WiFi conectada")

def llegada_mensaje(topic, msg):
    print("Mensaje recibido:", msg)
    if msg == b'bañoE':
        PinA.value(1)
        PinA2.value(1)
    elif msg == b'bañoA':
        PinA.value(0)
        PinA2.value(0)

def suscribir():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT,
                        user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(llegada_mensaje)
    try: 
        client.connect()
        client.subscribe(MQTT_TOPIC)
        print("Conectado al servidor MQTT en %s, suscrito al topic %s" % (MQTT_BROKER, MQTT_TOPIC))
    except Exception as e:
        print("Error al conectar al servidor MQTT:", e)
    return client

wifi_connect()
client = suscribir()

while True:
    try:
        client.wait_msg()
    except KeyboardInterrupt:
        print("\nDesconectando...")
        client.disconnect()
        break


