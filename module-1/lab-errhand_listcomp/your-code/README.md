# List Comprenhension

Los comentarios principales sobre el código se encuentran en el fichero main.py

Esta tarea me ha servido para afianzar los conocimientos de list comprenhension que tenía previamente al Bootcamp pero sobre todo para descubrir usos reales y funcionales que tienen fuera del mundo académico. El mejor ejemplo: 
```python
path = "../../../"
dirs = os.listdir(path)
files = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
print(files)
```

Con el manejo de excepciones con el bucle ```try/except``` el mejor ejemplo y el más didáctico me ha parecido el de programación defensiva: 
```python
while True: 
    try: 
        x = int(input('Introduce un entero: '))
    except ValueError as e: 
        print('Error: Entrada inválida, se espera un número entero') 
    else: 
        print(x*x)
        break
```
