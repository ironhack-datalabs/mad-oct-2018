# Pipeline Project


### Paso 1. Elegir dataset
Elegimos base de datos. BlackFriday.csv procedente de nuesto proyecto de Pandas. Escogemos el archivo que esta sin limpiar ya que vamos a intentar de seguir los mismos pasos que hicimos en la práctica. <br>
Copiamos el dataset en una nueva carpeta name "data". <br>

### Paso 2. Librerías
Creamos pipeline_miriam.py <br>
Instalamos libreria en nuestra terminal: "pip3 install matplotlib" y "pip3 install seaborn". <br>
Importamos las librerías necesarias: <br>
import pandas as pd <br>
import matplotlib.pyplot as plt <br>
import seaborn as sns <br>

#### Anexo 1 
Comprobamos que nuestra base de datos no tiene una entidad como "year" para que se pueda automatizar. Incluimos una nueva columna llamada "Year". <br>
import pandas as pd <br>
import numpy as np <br>
data = pd.read_csv('data/BlackFriday.csv') <br>
data['year'] = '2016' <br>
data.to_csv('data/blackfriday.csv', index=False) <br>

Nuestra dataset ha cambiado. Ha pasado de ser BlackFriday.csv a blackfriday.csv con la columna de 'year' añadida. <br>


### Paso 3. Data Acquisition
Obtenemos los datos de nuestro dataset. <br>
def acquire(): <br>
    data = pd.read_csv('data/blackfriday.csv') <br>
    return data <br>

### Paso 4. Definimos input
Nuestro input va a ser el año donde están grabados los datos. <br>
year = int(input('Please enter the year: ')) <br>

### Paso 5. Data Wrangling
Nuestro primer filtro va a ser por el año previamente definido. <br>
def wrangle(df): <br>
    filtered = data[data['Year']==year] <br>
    return filtered <br>

Ahora tenemos que limpiar nuestros datos. <br>

#### Renombramos columnas 
Renombramos columnas: 'Pursache' por 'Expenditure' (para que quede más claro que es el gasto por compras). Y 'City_Category' por 'City'. <br>

def renamed(data): <br>
    column_name = filtered.rename(columns={'Purchase':'Expenditure', 'City_Category': 'City'}) <br>
    return column_name <br>

#### Eliminamos columnas
Eliminamos columnas inecesarias que hacen que nuestra database sea más complicada de manejar. <br>
def drop_columns (data): <br>
    new_data = column_name.drop(column_name.columns[[5,6]], axis=1) <br>
    return new_data <br>

#### Ordenamos nuestras columnas 

def column_order (data): <br>
    col_order = ['User_ID', 'Product_ID', 'year', 'Gender', 'Age', 'City', 'Occupation', 'Marital_Status', 'Expenditure', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3'] <br>
    new_order = new_data[col_order] <br>
    return new_order <br>

#### Creamos nuvos niveles
def create_bins (data): <br>
    expend_labels = ['Low', 'Moderate', 'High', 'Very High'] <br>
    cutoffs = [0,6000, 12000, 18000, 24000] <br>
    bins = pd.cut(new_order['Expenditure'],cutoffs, labels=expend_labels) <br>
    new_order['Expend']=bins <br>
    return new_order <br>
He tenido problemas a la hora de añadir una nueva columna con las bins al dataframe, solución: dejar como salida de esta función 'new_order' la misma salida de la función anterior. <br>

### Paso 6. Data Analysis
Queremos saber por grupo de edades, cuáles son las que mayor media de gasto tienen. <br>
De momento, los bins que hemos creado no nos sirven pero en un análisis posterior puede que sí. 

def analyze(data): <br>
    grouped = new_order.groupby('Age').agg({'Expenditure':'mean'}).reset_index() <br>
    results = grouped.sort_values('Expenditure', ascending=False).head(10) <br>
    return results <br>

### Paso 7. Visualize

def save_visualize(data, title):
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=results, x='Age', y='Expenditure')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')

### Problemas
* Al definir la nueva columna con los valores de los bins creados. <br>
* En terminal funciona bien el pipeline. Warning de la función de bins me aparece también aunque el pipeline si funciona. <br>


