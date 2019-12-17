# Sequence Tagging - TP1 Introducción a PNL

En esta carpeta estan los arhicos correspondientes al primer trabajo práctico de la materia Introducción a PNL dictada por el Prof. Franco Luque durante Septiembre del 2019 en la UBA.

## Ejercicio 1
================

En el primer ejercicio estudiamos las propiedades y estadísticas del corpus Ancora. A continuación pegamos los resultados obtenidos de las estadísticas principales del corpus:

### Basic Statistics
|Dato|Conteo|
|----|------|
|sents| 17378| 
|tokens| 517194|
|words| 46501|
|tags| 85|

### Most Frequent POS Tags
|tag|freq|%|top|
|---|----|-|---|
|sp000|79884|15.45|(de, en, a, del, con)|
|nc0s000|63452|12.27|(presidente, equipo, partido, país, año)|
|da0000|54549|10.55|(la, el, los, las, El)|
|aq0000|33906|6.56|(pasado, gran, mayor, nuevo, próximo)|
|fc|30147|5.83|(,)|
|np00000|29111|5.63|(Gobierno, España, PP, Barcelona, Madrid)|
|nc0p000|27736|5.36|(años, millones, personas, países, días)|
|fp|17512|3.39|(.)|
|rg|15336|2.97|(más, hoy, también, ayer, ya)|
|cc|15023|2.90|(y, pero, o, Pero, e)|

### Word Ambiguity Levels
|n|words|%|top|
|-|-----|-|---|
|1|43972|94.56|(,, con, por, su, El)|
|2|2318|4.98|(el, en, y, ", los)|
|3|180|0.39|(de, la, ., un, no)|
|4|23|0.05|(que, a, dos, este, fue)|
|5|5|0.01|(mismo, cinco, medio, ocho, vista)|
|6|3|0.01|(una, como, uno)|
|7|0|0.00|()|
|8|0|0.00|()|
|9|0|0.00|()|

El código que genera estas estadisticas puede encontrarse en stats.py y en tp1_ej1_3.ipynb puede encontrarse como correrlo.

### Ejercicio 2

En este ejercicio implementamos dos *taggers* básicos como baseline. El primero de ellos etiqueta a todos los tokens con la etiqueta *nc0s000*. Los resultados obtenidos son:


Accuracy: 12.65% - 0.00% - 12.65% (total / known / unk)

|g \ m|sp000|nc0s000|da0000|aq0000|fc|nc0p000|rg|np00000|fp|cc|
|-----|-----|-------|------|------|--|-------|--|-------|--|--|
|sp000|-|14.39|-|-|-|-|-|-|-|-|
|nc0s000|-|12.65|-|-|-|-|-|-|-|-|
|da0000|-|9.70|-|-|-|-|-|-|-|-|
|aq0000|-|7.28|-|-|-|-|-|-|-|-|
|fc|-|5.85|-|-|-|-|-|-|-|-|
|nc0p000|-|5.53|-|-|-|-|-|-|-|-|
|rg|-|3.73|-|-|-|-|-|-|-|-|
|np00000|-|3.58|-|-|-|-|-|-|-|-|
|fp|-|3.55|-|-|-|-|-|-|-|-|
|cc|-|3.41|-|-|-|-|-|-|-|-|


El segundo baseline es el etiquetar a cada token con el tag más frecuente con el que aparece, y los resultados obtenidos son:

Accuracy: 87.58% - 95.27% - 18.01% (total / known / unk).

|g \ m|sp000|nc0s000|da0000|aq0000|fc|nc0p000|rg|np00000|fp|cc|
|-----|-----|-------|------|------|--|-------|--|-------|--|--|
|sp000|14.28|0.05|-|-|-|-|0.01|-|-|-|
|nc0s000|0.00|12.22|-|0.24|-|0.00|0.03|0.00|-|0.00|
|da0000|-|0.15|9.54|-|-|-|-|-|-|-|
|aq0000|0.01|2.05|-|4.84|-|0.13|0.00|-|-|-|
|fc|-|-|-|-|5.85|-|-|-|-|-|
|nc0p000|-|1.24|-|0.21|-|4.07|-|-|-|-|
|rg|0.02|0.31|-|0.03|-|-|3.29|-|-|0.02|
|np00000|0.00|2.04|-|0.00|-|0.00|-|1.52|-|0.00|
|fp|-|-|-|-|-|-|-|-|3.55|-|
|cc|0.00|0.01|-|-|-|-|0.05|0.00|-|3.34|

Aca podemos observar un mapa de calor de las etiquetas para facilitar la interpretación de los resultados:

![hm0](latestfig_0.png)

### Ejercicio 3

En este ejercicio buscamos utilizar 

### Ejercicio 4

### Ejercicio 5
