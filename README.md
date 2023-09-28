# Personaje

## Nombre del personaje
Pastor con fuego  🔥

## Materiales utilizados
|Nombre de Componente|Descripción del componente|Cantidad|Precio|
|--|--|--|--|
|ESP32|Microcontrolador con comunicación serial, wifi, bluetooth|1|$140.00|
|Cables Dupont|Cables MM HH HM para conexión de prototipos|50|$60.00| 
|Servomotor|||||

## Software Utilizado
|Nombre de Software|Versión|Tipo|
|--|--|--|
|Thonny|4.1.2|Software Libre|
|SQlite|3.12.2|Software Libre (Gestor de Base de Datos)|
|Visual Studio Code|1.82.2|Software Libre (Editor de código fuente independiente)|
|Platformio IDE|3.3.0|Software Libre (Herramienta Desarrollo C)|
|Arduino IDE|2.2.1|Aplicación multiplataforma|

## Dibujo del prototipo a desarrollar
Coloca el dibujo a mano de la propuesta de prototipo a desarrollar
![Imagen del Prototipo](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Pastor%20con%20Fuego.jpg?raw=true)

## Comunicación
Describir el protocolo de comunicación que tendra el dispositivo. Describir o hablar sobre como va a interactuar un dispositivo móvil.
Como se conecta o como mandar una orden al dispositivo. (Cómo interactua el usuario con el prototipo)

Para crear un prototipo de un pastor eléctrico que se conecta a través de una placa ESP32 y utilizar sensores para emitir luz, sonido y moverse, estamos considerando la comunicación y la interacción con el usuario. Nos basamos en el uso de tecnologías inalámbricas comunes, como Wi-fi o Bluetooth.
A continuación se describe como podría funcionar: 

Wi-Fi o Bluetooth: La placa ESP32 podría estar equipada con módulos Wi-Fi o Bluetooth para la comunicación. Estas tecnologías permiten que el dispositivo sea detectado y controlado por un dispositivo móvil cercano.
Configuración Inicial: Cuando el dispositivo se encienda por primera vez o entre en modo de configuración, podría actuar como un punto de acceso Wi-Fi o activar la función de emparejamiento Bluetooth. El usuario podría conectarse a este punto de acceso o emparejar el dispositivo desde su dispositivo móvil.
Aplicación Móvil: El usuario podría descargar una aplicación móvil específica para interactuar con el pastor eléctrico.
Interfaz de Usuario: La aplicación móvil proporcionaría una interfaz de usuario que permite al usuario configurar y controlar el pastor eléctrico. Esto incluiría ajustar la intensidad de la luz, mover las partes movibles, que podría ser la mano para hacer un saludo y emitir el sonido.

## Arquitectura
Colocar una imagen donde coloques los sensores, los actuadores, el microcontrolador, base de datos (sqlite o mysql)
![Imagen de los componentes, la arquitectura]()

## Base de Datos
Colocar una imagen del modelo relacional de la base de datos (2 tablas) tabla de sensores y actuadores
![Imagen del modelo relacional de la base de datos]()
