# Personaje (Proyecto IoT)

## Integrantes del equipo
**GRUPO - GDS0542**  
Herrera Ramiro - 1222100418  
Ortega Rentería María Roxana - 1222100822

## Nombre del personaje
Pastor con Fogata  🔥

## Materiales utilizados
|Nombre de Componente|Descripción del componente|Cantidad|Precio|
|--|--|--|--|
|ESP32|Microcontrolador con comunicación serial, wifi, bluetooth|2|$280.00|
|Cables Dupont|Cables MM HH HM para conexión de prototipos|50|$60.00| 
|Servomotor|Motor que permite el control de posición angular|1|$60|
|Luces LED|Diodos emisores de luz para iluminación| 2 azules, 8 rojos, 2 amarillos|$20|
|Altavoces o zumbadores|Dispositivos para reproducción de sonido o generación de zumbidos|1|$15|
|Sensor de Movimiento(PIR)|Sensor que detecta movimientos en su entorno|1|$60|
|Protoboard|Placa de pruebas para conectar y proteger los pines del microcontrolador|1|$100|
|HCSR04|sensor de distancias por ultrasonidos capaz de detectar objetos y calcular la distancia a la que se encuentra en un rango de 2 a 450 cm|1|$100|
|Motor a pasos|Motor que convierte pulsos eléctricos en movimientos angulares discretos|1|$100|
|Materiales para el diseño|Telas/Madera/Alambron/Silicón/Pegamento|varios|$45|
|||**TOTAL**|$740|



## Software Utilizado (Testeo y Elaboración)
|Nombre de Software|Versión|Tipo|
|--|--|--|
|Thonny|4.1.2|Software Libre|
|SQlite|3.12.2|Software Libre (Gestor de Base de Datos)|
|Visual Studio Code|1.82.2|Software Libre (Editor de código fuente independiente)|
|Platformio IDE|3.3.0|Software Libre (Herramienta Desarrollo C)|
|Arduino IDE|2.2.1|Aplicación multiplataforma|
|WokWi|--|Entorno virtual de pruebas con componentes|

## Dibujo del prototipo a desarrollar
Visualización previa del diseño a elaborar respecto a los requisitos solicitados desde el principio
![Imagen del Prototipo](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Pastor%20con%20Fuego.jpg?raw=true)

## Circuito en wokwi de los componentes electronicos conectados
(imagen donde se muestren varias imagenes para hacer luz, sonido y movimiento)
![Conexión del Prototipo](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/ConeccionWokwi.jpg)
![Codigo parte 1](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/CodigoWokwi1.jpg)
![Codigo parte 2](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/CodigoWokwi2.jpg)
![Codigo parte 3](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/CodigoWokwi3.jpg)

## Comunicación
A continuación se anexa la descripción del protocolo de comunicación que tiene el dispositivo. Explicando y describiendo como interactua un usuario con el proyecto y como interactua con un dispositivo móvil.

Para crear un prototipo de un pastor eléctrico que se conecta a través de una placa ESP32 y utilizar sensores para emitir luz, sonido y moverse, se consideró la comunicación y la interacción con el usuario de manera dinámica. Nos basamos en el uso de tecnologías inalámbricas comunes, como Wi-fi o Bluetooth, seleccionando el uso de Wi-fi como medio de comunicación. Así mismo, mediante código implementado el cuál conecta la placa a una red y suscribe a un servicio para conexión, permite generar la interacción.

A continuación se describe como funciona: 

* **Wi-Fi:** La placa ESP32 se encuentra conectada a un broker el cuál funciona como punto de acceso para la conexión entre comunicaciones.  Estas tecnologías permiten que el dispositivo sea detectado y controlado por un dispositivo móvil cercano al dar de alta el servicio de Node-red.
* **Configuración Inicial:** Cuando el broker está dado de alta y de igual manera el servicio de Node-red, el dispositivo se encienda y permite la conexión. El usuario puede conectarse a este punto de acceso o red y mediante Node-red o la aplicación móvil de la misma controlar leds y movimiento del motor a pasos.
* **Aplicación Móvil:** El usuario debe descargar una aplicación móvil específica para interactuar con el pastor eléctrico.
* **Interfaz de Usuario:** La aplicación móvil proporcionaría una interfaz de usuario que permite al usuario configurar y controlar el pastor eléctrico. Esto incluiría ajustar la intensidad de la luz (encender y apagar leds), mover las partes movibles (interactuar con el motor a pasos).

## Arquitectura
Colocar una imagen donde coloques los sensores, los actuadores, el microcontrolador, base de datos (sqlite o mysql)
![Imagen de los componentes, la arquitectura](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Arquitectura.jpg?raw=true)

## Base de Datos
Colocar una imagen del modelo relacional de la base de datos (2 tablas) tabla de sensores y actuadores
![Imagen del modelo relacional de la base de datos](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Modelo%20Relacional%20BD.jpg?raw=true)

# Documentación del Proyecto

## Video del funcionamiento
A conticuación se anexa un video el cuál explica la funcionalidad del proyecto, así como sus componentes a grandes rasgos y de manera general:
[Enlace a video dentro de drive](https://drive.google.com/file/d/1hHGCqCIDn4_4PeWZ1XXJfEMAypk7ssv7/view?usp=sharing)


## Código implementado
Dentro del presente repositorio se encuentran las carpetas respectivas donde se puede visualizar los archivos de código.

## Imagenes del proceso de elaboración
A continuación se anexan pruebas del proceso de elaboración mediante diversas imagenes o fotos que se capturaron durante la elaboración.

![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Componentes.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Elaboracion%201.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Equipos%20trabajando.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Referencia%20tamanio.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Retoques.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Ultimos%20ajustes.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/conexion%20componentes.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/prueba%20de%20cableado.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/trabajo%20elaboracion.jpg)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Finalizado.jpg)


## Imagenes de elaboración del código
A continuación se anexan pruebas del proceso de elaboración del código medante capturas del entorno.
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Evidencia%20codigo.png)  
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Evidencia%20codigo%202.png)

## Flujo de Node-red
Se anexa el flujo de Node-red, además se agrega el archivo dentro del presente repositorio.
![Img](https://github.com/RamiroHerreraX/Personaje/blob/main/imagenes/Flujo%20NodeRed.jpg)
