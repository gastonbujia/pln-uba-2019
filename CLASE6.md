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

### Contextual Representations - ELMo

Hasta aca vimos Word2Vec, GloVe (W2V que incluia una versión probabilístca) y fastText que trabaja a nivel de caracteres y n-grams. Algunas críticas a los *word embbedigs*:

- Único word embedding para una palabra con ambiguos sentidos --> posible solición desambiguar a mano y tener un embedding para cada uno (no es una tarea fácil).
- *

Pero en RNN ya metimos contexto, ¿podemos combinarlos? Ahi aparece la idea de usar un modelo de sequencias pre-entrenado

***TAG LM - 2017*** (pre-ELMo)
Entrenamos por un lado un lenguaje pre-contextualizado con una bi-LSTM y por el otro usamos word embbedigs contextualizados. Otro modelo similar ***CoVe*** (Contextualized Vectors).

***ELMo - 2018*** (Embeddings Language Models)
Hasta el anterior los modelos solo pudieron mejorar el state-of-the-art de una sola tarea, mientas que este modelo pudo mejorar en al menos 6 tareas a la vez.

- Entrena una BILSTM
- Mete dos capas biLSTM
- Usa una CNN a nivel de caracteres
- Despues ELMo necesita un word embedding que este libre de contexto, por ejemplo NO w2v.

Después aparece también ULMfit con *learning rates* variables y otros pequeños *fine-tunning*. Además devuelve los vectores contextualizados con una concatenación de maxpool y meanpool.

### Transformers - BERT

En el decoder desaparece el valor de la hidden state y aparece un key-value par para codificar este hidden state per desacoplando sus valores. Además agregan *positional enconding* utilizando funciones senos y cosenos y también agregan residual conections. Tiene muchos detalles técnicos. Lo malo de los transformers es que no se llevan bien con otras arquitecturas de DNN como por ejemplo las LSTM. Lo bueno, le gano a todos en muchas tareas,

Dos ejemplo son ***BERT*** y ***GPT***. En BERT se le dice bidireccional aunque no en el sentido de las LSTM ya que no recorre en ambos sentidos sino porque mira la attention de todos contra todos con algún masking.

BERT fue testeado en GLUE tasks que mide varias tareas del lenguaje natural y mejoro mucho el estado del arte en todas las tareas, ya incluso usando solo el modelo y nada de fine-tunning ni cosas raras.

### Attention is all you need - self-attention

EL modelo contado por los mismos autores y con otros gráficos.