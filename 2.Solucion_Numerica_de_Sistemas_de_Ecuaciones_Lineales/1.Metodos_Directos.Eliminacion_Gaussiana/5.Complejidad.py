'''
El número de operaciones que realizan los métodos directos para la
resolución de sistemas de ecuaciones lineales es de orden n3 , donde
n es la dimensión del sistema.
1. Eliminación de Gauss: O(n^3 ).
2. Gauss-Jordan: O(n^3 ) (con más operaciones debido a la
eliminación hacia atrás).
3. Pivotación Parcial: O(n^3 ) + un costo adicional bajo por el
intercambio de filas.
4. Pivotación Total: O(n^3 ) + un costo adicional mayor por el
intercambio de filas y columnas.
'''
'''
Conclusiones
1. El método de eliminación de Gauss es eficiente para sistemas
grandes y es una de las técnicas más utilizadas en la práctica.
2. Aunque el algoritmo Gauss-Jordan es muy directo para
encontrar la inversa de una matriz, es generalmente más
costoso que la eliminación de Gauss debido al doble proceso
de eliminación hacia adelante y hacia atrás.
3. La pivotación parcial es una técnica crucial para la
estabilidad de los cálculos, y su costo adicional es
relativamente bajo en comparación con los métodos sin
pivotación.
4. La pivotación total mejora la precisión numérica, pero
aumenta el costo computacional debido a la doble búsqueda
de elementos máximos (filas y columnas).
5. La eliminación de Gauss es el más eficiente, seguido de la
pivotación parcial, luego Gauss-Jordan, y finalmente la
pivotación total.
6. La pivotación aumenta el costo computacional. Sin embargo,
la pivotación es esencial cuando se trata de mejorar la
estabilidad numérica, especialmente para matrices mal
condicionadas.
¿Por qué importa la estabilidad?
▶ La eliminación gaussiana es un método directo para resolver
sistemas lineales.
▶ La estabilidad numérica es clave para obtener soluciones
precisas.
▶ El manejo del pivote durante el proceso determina el
comportamiento del método.
Sin Pivoteo
▶ Puede ser numéricamente inestable.
▶ Si el pivote es muy pequeño, se amplifican los errores por
redondeo.
▶ Puede fallar incluso con matrices bien condicionadas.
Con Pivoteo Parcial (Recomendado)
▶ Se intercambian filas para que el pivote sea el mayor en valor
absoluto en su columna.
▶ Es el método estándar en la práctica.
▶ Proporciona buena estabilidad y bajo costo computacional.
Con Pivoteo Completo
▶ Se intercambian filas y columnas.
▶ Asegura el pivote de mayor magnitud absoluta posible.
▶ Máxima estabilidad, pero mayor costo computacional.
▶ Rara vez necesario en la práctica.
Comparación
▶ Sin pivoteo: rápido, pero puede fallar.
▶ Pivoteo parcial: equilibrio ideal entre eficiencia y estabilidad.
▶ Pivoteo completo: máxima estabilidad, pero raramente
necesario.
'''
'''
Una matriz mal condicionada es una matriz que amplifica mucho los errores numéricos al resolver sistemas lineales del tipo 
Ax=b. Es decir, pequeños errores en los datos o en los cálculos pueden provocar grandes errores en la solución.
El número de condición de una matriz A, denotado como 
κ(A), mide cuán sensible es la solución del sistema Ax=b ante cambios en los datos.
    κ(A)=∥A∥⋅∥A−1∥
Si κ(A)≈1: la matriz está bien condicionada (estable numéricamente).
Si κ(A)≫1: la matriz está mal condicionada.
Si κ(A)→∞: la matriz es casi singular (o exactamente singular si no tiene inversa).
'''

'''
Las normas se usan para medir el "tamaño" de una matriz y tienen diferentes definiciones y aplicaciones.
Norma 1 (norma columna): 
La norma 1 de una matriz A es el máximo de las sumas de los valores absolutos de las columnas de la matriz:
Norma 2 (norma espectral o norma Euclidiana): 
La norma 2 de una matriz A se define como el mayor valor singular de la matriz:
Norma infinito (norma fila): 
La norma infinito de una matriz A es el máximo de las sumas de los valores absolutos de las filas de la matriz:
'''
