# Matplot y Seaborn

Estas son las cuestiones resultantes del lab:

### Challenge 1

Respuestas a 3, 5 y 6 por ej. salen con un código como este: 

```
[<matplotlib.lines.Line2D at 0x7f010b0d0da0>]
```

Esto no parece una descripción de objeto, parece sólo de la posición en memoria. Porqué sale?  (Entiendo que si hago una asignación dejará de salir, pero en qué casos sale? 

Indexex below some binned histograms, don't  correspond to the graphic. For example the distribution of 'Age' variable with 10, 20, 50 bins, see the biggest bins clearly don fit the numbers. 



#### Use the appropriate plot to visualize the column `Gender`

How do I set different colors for each bar. Seems I have to use a palette? 

#### Use the appropriate plot to visualize the column `Pclass`

Can't enter three colors with names, like

color=('darkblue', 'purple', 'darkred')

it thinks Iḿ passing RGB values. But I cant even giving RGBs: 

()'#00008b', '#800080', '#8B0000')  

nor without the 'quotes '



### Wtf is faceting? (seaborn). Is the same as axes in matplotlib?

https://seaborn.pydata.org/generated/seaborn.FacetGrid.html?highlight=facetgrid