# Notas ultima clase - Machine Translation - Encoders y Transformers

### Primero SMT - 1990 - 2010

Antes que esto estuvo las correspondencias de palabras uno a uno y luego pararecieron los primeros modelos probabilistas del lenguaje. Phrased-Based SMT y Syntaxis SMT. Andaba mas o menos bien pero con muchos problemas.

### Sigue NMT - Neural Machine Translation - Modelos sequence to sequence

Empieza a aplicarse modelos de redes neuronales con encoders vanilla (no bidireccional). Estos modelos seq2seq son muy versátiles y se usan en resúmenes, diálogos, parsing y generación de código. 

Bleu - Bilingual Evaluation Understandig - es la métrica que se usa para evaluar estos sistemas que depende de por ejemplo si se usan n-grams y penalidades. Sin embargo no es perfecto

Esta resuelto? No, tiene problemas de bias por la data. Ejemplo de traducción del malayo al inglés, traduce el genero neutro del malayo al femenino o masculino dependiendo del trabajo. Ejemplo del ag aga ag ag en somalie a algo biblico, el problema es el tamaño del corpus y el peso de la biblia, el libro mas traducido en todos los idiomas, tiene mayor peso.

El problema de bottleneck del encoder, toda la información de una sola oración la mete en un solo vector sin importar el largo de la oración.

### Attention seq2seq

Para solucionar el problema este aparece attention y el modelo que surge *sequence to sequence with attention*. Antes el decoder y el enconder tenian hidden states que no tenian porque estar en el mismo espacio, ahora con attention no sumamos nuevos parametros sino que logramos vincular los hidden states del enconder con decoder como si fueran skip-connections. En todo caso sumo parámetros en las unidades LSTM del decoder. Al final sumamos una capa de softmax para terminar la parte de atención.

Asi esto nos aliviana dos dificultades, el problema de cuello de botella al conectar la información en distintos puntos gracias a estas conecciones y tambien con el problema de *vanishing gradients*.

También los *attention scores* nos dan una interpretabilidad del modelo viendo que parte atiende de la oración, *soft querys*.

### Attention Scores Variants

Existen varias variantes para el problema de calcular los *attention scores*

- Basic Dot Product = state x hidden^t
- Multiplicative Attention = state x W x hidden^t
- More transformations

### Question Answering (text)

- SQuAD Dataset de Stanford, donde tenes un texto y tenes que encontrar la respuesta en el texto.
- SQuAD 2.0 Ahora las respuestas no estan necesariamente en el texto como en el dataset 1.0.

### Contextual Representations

Hasta aca vimos Word2Vec, GloVe (W2V que incluia una versión probabilístca) y fastText que trabaja a nivel de caracteres y n-grams. Algunas críticas a los *word embbedigs*:

- Único word embedding para una palabra con ambiguos sentidos --> posible solición desambiguar a mano y tener un embedding para cada uno (no es una tarea fácil).
- 