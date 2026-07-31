

# Recuperación de Información con Vector Space Model para Artículo de Noticias

Este proyecto tiene como objetivo crear un sistema de recuperación de información para artículos de noticias. El algoritmo utilizado en este proyecto es el algoritmo Vector Space Model, con su evaluación utilizando Mean Average Precision (MAP), Precision@K y R-Precision. Los datos utilizados son artículos de noticias obtenidos del sitio Kumparan. Hay 60 artículos de noticias en 3 categorías (Política, Tecnología, Travel). Cada categoría contiene 20 artículos de noticias. Además, en este proyecto se han configurado 4 escenarios, a saber:
1. Sin Stemming - Con Stopword: <br>
    En este escenario, no se aplica el proceso de stemming a cada documento y las stopword presentes en los documentos se mantienen.
2. Sin Stemming - Sin Stopword: <br>
    En este escenario, no se aplica el proceso de stemming a cada documento y las stopword presentes en los documentos no se utilizan (se eliminan las stopword).
3. Con Stemming - Con Stopword: <br>
    En este escenario, se aplica el proceso de stemming a cada documento y las stopword presentes en los documentos se mantienen.
4. Con Stemming - Sin Stopword: <br>
    En este escenario, se aplica el proceso de stemming a cada documento y las stopword presentes en los documentos no se utilizan (se eliminan las stopword).

Tras realizar las pruebas utilizando la evaluación Mean Average Precision, se obtuvieron los siguientes resultados:
1. Escenario 2 – Sin Stemming Sin Stopword 		=> 0.8028486394557823
2. Escenario 4 – Con Stemming Sin Stopword 		=> 0.7900198885109599
3. Escenario 1 – Sin  Stemming Con Stopword 	=> 0.7748469387755103
4. Escenario 3 – Con Stemming Con Stopword 	=> 0.7668191609977324

Como se puede observar en los resultados de la evaluación, el escenario "sin stopword" es mejor en cuanto a precisión en comparación con el escenario "con stopword". Esto se debe a que las palabras menos importantes (stopword) se eliminan del corpus existente. Si no se realiza la eliminación de las palabras presentes en la lista de stopword, dichas palabras se ponderarán, y dado que están presentes en casi todos los documentos, esto afectará el resultado de la cosine similarity; posteriormente, al realizar el proceso de information retrieval, habrá muchos documentos irrelevantes en los primeros puestos. Por lo tanto, la eliminación de las palabras que son stopword tiene como objetivo que solo las palabras importantes y relevantes se utilicen como términos en la ponderación. 
De los resultados de evaluación anteriores también se obtiene que el uso de stemming no afecta significativamente el nivel de precisión. Esto se debe a que el proceso de stemming no es perfecto (ya sea over-stemming o under-stemming).
