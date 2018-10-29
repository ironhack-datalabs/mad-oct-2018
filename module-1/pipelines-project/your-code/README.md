# Pipeline Proyect

**email**: garcia.cobo.alberto@gmail.com
**tags**: pipeline, pandas, seaborn, automatization

### Descripción

En este entregable se pretende separar las 4 fases que caracterizan un pipeline: 

* Acquisition
* Wrangling
* Analysis
* Reporting

### Dificultades
#### 1. Variables
En este entregable la mayor dificultad ha sido la transición de las variables globales de una versión en jupyter notebook de proyectos anteriores a la programación funcional. 

Para ejecutar el código imprimir por pantalla:
```
$ python3 main.py
```
#### 2. Librerías
Si durante la ejecución ocurre un mensaje de error tal que así: 
```
import tkinter as Tk
ModuleNotFoundError: No module named 'tkinter'
```
Tras revisar la documentación y recordar el diagrama de capas del Sistema Operativo respecto a Python, hay que instalar tkinter, pero en el SO, no en pip3
```
$ sudo apt-get install python3-tk
```
Esta solución la he puesto para los compañeros en la plataforma Slack
