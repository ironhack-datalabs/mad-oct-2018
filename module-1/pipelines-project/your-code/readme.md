Escojo la misma base de datos que utilicé para Pandas Project, que es una base de datos que muestra el índice de felicidad por país en función de una serie de variables.

Importo las librerias necesarias y  comienzo el tratado de datos. Hago un display de los valores Happy Score por país y region ordenados por orden descendente y  veo que hay dos datos que exceden con mucho la media.

Intento modificarlos de varias maneras pero finalmente la única forma de conseguirlo es mediante data loc localizarlos y sustituirlos por valores concretos. A pesar de hacer un display y comprobar que los valores han cambiado en el dataframe data, al obtener el gráfico observo que las barras no reflejan correctamente las columnas, ya que dos de ellas son excepcionalmente altas.

Refresco repetidas veces todas las ejecuciones pero no hay manera de que se sincronice el dataframe final con ese tratamiento de datos.

La práctica me parece muy interesante, ver todos los códigos que hemos ido contruyendo hasta ahora por partes ejecutarse de una sola vez. Es una pena no poder hacer algo más completo, me hubiera gustado añadir los datos de otras dos tablas csv correspondientes a otros dos años y haber hecho la limpieza con más funciones pero me ha resultado imposible. En general no he tardado mucho en construirlo, pero en el tratamiento de esos dos datos concretos he empleado varias horas para finalmente no conseguir el objetivo que buscaba.