# PANDAS PROYECTO
## Paso 1. Elegir una database
He escogido las ventas en blackfriday. Base de datos de Kaggle  (https://www.kaggle.com/mehdidag/black-friday) <br>
Analizando nuestra hipótesis principal es extraer los datos de gasto en compras por rango de edad y por status. <br>
Para ello, asumimos que "Purchase" contiene los valores en $ del gasto de compra por cada usuario. <br>
Comenzamos a limpiar los datos. <br>

## Paso 2. Crear nuevo dataframe
Creamos un nuevo dataframe con las columnas que necesitamos para nuestra hipotésis. <br>

blackfriday = data[['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category', 'Marital_Status', 'Purchase']]
display(blackfriday.head())<br>

## Paso 3. Renombrar entidades. 
Renombramos las entidades de nuestro dataframe blackfriday. <br>
blackfriday = blackfriday.rename(columns={'Purchase':'Expenditure',
                              'City_Category': 'City'}) <br>
display(blackfriday.head()) <br>

## Paso 4. Renombramos datos. 
Para poder entender los datos vamos a renombrar los atributos de algunas columnas. <br>
Primero comprobamos el tipo de dato de nuestro datafram. <br>

blackfriday.info()<br>

Queremos modificar City para darle una ciudad a A, B y C. Y es un objeto por lo que podemos modificarlo utilizando string. <br>

Para poder asignar "Single" y "Married" a los valores 0 y 1 de la columna "Marital_Status" tenemos que cambiar el tipo de datos. <br>

blackfriday['Marital_Status'] = blackfriday['Marital_Status'].astype('str')<br>
blackfriday.loc[blackfriday['Marital_Status'].str.startswith('0'), 'Status'] = 'Soltero'<br>
blackfriday.loc[blackfriday['Marital_Status'].str.startswith('1'), 'Status'] = 'Casado'<br>
display(blackfriday.head())<br>

## Paso 5. Eliminar columnas. <br>
Para tener nuestra base de datos mas limpia, eliminamos las columnas que no nos son relevantes. <br>
Eliminamos las columnas de "Marital_Status" y "City"<br>

blackfriday = blackfriday.drop(blackfriday.columns[[5,6]], axis=1)<br>
display(blackfriday.head()) <br>

Ordenamos las columnas para dejar "Expenditure" en la última columna ya que es lo que más adelante vamos a contrastar. 

## Paso 6. Valores nulos
Comprobamos si tenemos valores nulos. <br>
null_cols = blackfriday.isnull().sum()<br>
print(null_cols)<br>

Al no tener valores nulos no tenemos que eliminar. En el caso en el que tuvieramos, como todas las columnas que tenemos nos pueden ser de importancia, rellenaríamos esos datos con (0). <br>
Imaginemos que pueden estar en la columna 'Expenditure'. Aplicaríamos en 'Expenditure' esta función: blackfriday[['Expenditure']] = blackfriday[['Expenditure']].fillna(0) <br>

## Paso 7. Distribución en bins
Para poder conocer la distribucion de nuestros datos, calculamos mean, min, max, Q1 y Q3. 

blackfriday['Expenditure'].max()
blackfriday['Expenditure'].min()
blackfriday['Expenditure'].mean()
blackfriday['Expenditure'].quantile(0.25)
blackfriday['Expenditure'].quantile(0.75)

Sabemos que el 50% de los valores del gasto en compra se encuentran entre 5866 y 12073 (referencia en readme.md de foto). Por lo que serían los valores de corte de nuestras bins. Con ello conseguimos unos bins en low y high mucho más precisos. <br>

Definimos los niveles de corte <br>
expend_labels = ['Low', 'Moderate', 'High', 'Very High'] <br>

Definimos los valores de corte de manera uniforme <br>
cutoffs = [0,6000, 12000, 18000, 24000]
bins = pd.cut(blackfriday['Expenditure'],cutoffs, labels=expend_labels)
bins.head(20)

Para conocer el número de valores que hay en cada bin. <br>
bins.value_counts()
Aproximadamente 50% de los usuarios han tenido un nivel de gasto moderado. 

## Paso 8. Incluir valores de bins en blackfriday

Definimos un nuevo dataframe con nuestro dataframe original y agregamos la columna bins. <br>

black_f = pd.DataFrame(blackfriday)
black_f['Expend_type']=bins
display(black_f.head())

## Paso 9. Conclusiones
### 1. Perfil del consumidor más concurrido
Las personas solteras de más de 55 años y con un gasto muy alto ha sido el perfil más concurrido. <br>


black_f.groupby(['Expenditure','Age', 'Status', 'Expend_type']).size().reset_index().max()

### 2. Single vs. Married

black_f.groupby(['Status','Expend_type']).size().reset_index()

Podemos comprobar que los solteros son más propensos a las compras durante el BlackFriday. Los datos nos muestran un mayor número de personas solteras que casadas. El nivel de gasto más común es el moderado en ambos tipos, hecho que recalca nuestros datos extraidos anteriormente ya que el rango más comun de gasto en nuestra dataset es el "moderado". <br>

### 3. Tipo de gasto por edades
En todas las edades un gasto moderado es el más común. <br>
La franja de edad entre 26-35 años es la más concurrida en todos los rangos de gasto. <br>

black_f.groupby(['Age','Expend_type']).size().reset_index()

## Paso 10. Exportamos datos
Creamos una carpeta local y un fichero csv al que vamos a exportar los datos. 
black_f.to_csv('black_f/black_f.csv', index=False)


## Problemas 
* Identificar las funciones para extraer los datos que quiero analiar. <br>
* He tenido que modificar las etiquetas de mis datos para añadir un nivel más, la mayoría de mis datos están en rango 'moderado'. <br>