# Project: API REST


---

## Elección del API

Analizando las [APIs publicas de GitHub](https://github.com/toddmotto/public-apis) pude ver [ipinfo.io](https://ipinfo.io/) una **plataforma que introduciendo la dirección IP y te localiza el dispositivo**. La idea me gusto y me puse a buscar la info de su API.

## Analisis del API de ipinfo.io

En un primer vistazo encontré que para peticiones individuales de IPs no necesitaba autentificación y no lo dudé, me puse a ello. En estas primeras pruebas, se me ocurrió la idea de poder ubicar en un mapa la dirección de la IP.

## Analisis del JSON de ipinfo.io

El JSON que se genera tiene las siguientes Keys:(ip, city, region, country, loc y postal). De estas Keys la que quiero obtener es la latitud y longitud (Para un ejemplo cuya IP sea **212.170.222.26** obtienes **40.4165,-3.7026**).

## Analisis de GoogleMaps

Una vez obtengo la localización de la IP lo que quiero es poder ubicarla en GoogleMaps. Para ello me leo la documentación de Google y me registro para la obtener la **API_key**. Con ella intento generar la visualización en Maps pero no lo consigo.

## Analisis de webbrowser.py

Al no encontrar la documentación intenté buscar una libreria en Python con la que poder hacerlo, y encontré [webbrowser.py](https://docs.python.org/2/library/webbrowser.html). Esta librería genera una apertira del navegador con las coordenadas que previamente obtuve.

## Limpieza del código

Realice una limpieza del codigo y introduge un imput para poder introducir la dirección IP. con ello terminé el ejercicio.