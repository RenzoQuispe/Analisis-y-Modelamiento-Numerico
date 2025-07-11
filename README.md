# Análisis y Modelamiento Numérico

Repositorio de prácticas y algoritmos del curso Análisis y Modelamiento Numérico, organizados por temas y métodos

## Índice de Contenidos

### 1. [Análisis de Errores](./1.Analisis_de_Errores/readme.md)

---

### 2. [Solución Numérica de Sistemas de Ecuaciones Lineales](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales)

- **[Métodos Directos - Eliminación Gaussiana](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/1.Metodos_Directos.Eliminacion_Gaussiana)**
  - [Eliminación Gauss sin Pivoteo](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/1.Metodos_Directos.Eliminacion_Gaussiana/1.EliminacionGaussSinPivoteo.py)
  - [Gauss-Jordan](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/1.Metodos_Directos.Eliminacion_Gaussiana/2.MetodoGaussJordan.py)
  - [Pivoteo Parcial](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/1.Metodos_Directos.Eliminacion_Gaussiana/3.PivoteoParcial.py)
  - [Pivoteo Total](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/1.Metodos_Directos.Eliminacion_Gaussiana/4.PivoteoTotal.py)
  - [Análisis de Complejidad](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/1.Metodos_Directos.Eliminacion_Gaussiana/5.Complejidad.py)

- **[Factorización](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/2.Factorizacion)**
  - [LU](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/2.Factorizacion/1.FactorizacionLU.py)
  - [Cholesky](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/2.Factorizacion/2.FactorizacionCholesky.py)

- **[Técnicas de Factorización LU](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/3.Tecnicas_de_Factorizacion_LU)**
  - [Crout](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/3.Tecnicas_de_Factorizacion_LU/1.MetodoCrout.py)
  - [Crout Tridiagonal](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/3.Tecnicas_de_Factorizacion_LU/2.CroutTridiagonal.py)
  - [Doolittle](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/3.Tecnicas_de_Factorizacion_LU/3.MetodoDoolitle.py)

- **[Métodos Indirectos](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/4.Metodos_Indirectos)**
  - [Jacobi](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/4.Metodos_Indirectos/1.Metodo_de_Jacobi.py)
  - [Gauss-Seidel](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/4.Metodos_Indirectos/2.Metodo_de_Gauss-Seidel.py)
  - [SOR (Relajación)](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/4.Metodos_Indirectos/3.Metodo_de_Relajacion_SOR.py)

- **[Métodos de Minimización para Resolver Ax = b](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/5.Metodos%20de%20Minimizaci%C3%B3n%20para%20Resolver%20Ax%20=%20b)**
  - [Descenso Coordinado](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/5.Metodos%20de%20Minimizaci%C3%B3n%20para%20Resolver%20Ax%20=%20b/1.Metodo_del_Descenso_Coordenado.py)
  - [Descenso Relajado](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/5.Metodos%20de%20Minimizaci%C3%B3n%20para%20Resolver%20Ax%20=%20b/2.Metodo_del_Descenso_Relajado.py)
  - [Cauchy](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/5.Metodos%20de%20Minimizaci%C3%B3n%20para%20Resolver%20Ax%20=%20b/3.Metodo_de_Cauchy.py)
  - [Gradiente Conjugado](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/5.Metodos%20de%20Minimizaci%C3%B3n%20para%20Resolver%20Ax%20=%20b/4.Metodo_de_Gradiente_Conjugado.py)
  - [Conclusiones](./2.Solucion_Numerica_de_Sistemas_de_Ecuaciones_Lineales/5.Metodos%20de%20Minimizaci%C3%B3n%20para%20Resolver%20Ax%20=%20b/Conclusiones.txt)

---

### 3. [Solución Numérica de Sistemas de Ecuaciones No Lineales](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales)

- **Localización de Raíces I**
  - [Bisección](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/Metodos%20de%20localizacion%20de%20raices%20I/Metodo_de_la_Biseccion.py)
  - [Regla Falsa](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/Metodos%20de%20localizacion%20de%20raices%20I/Metodo_de_la_Regla_Falsa.py)

- **Localización de Raíces II**
  - [Secante](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/Metodos%20de%20localizacion%20de%20raices%20II/Metodo_de_la_Secante.py)
  - [Punto Fijo](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/Metodos%20de%20localizacion%20de%20raices%20II/Metodo_del_Punto_Fijo.py)

- **Localización de Raíces III**
  - [Newton-Raphson](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/Metodos%20de%20localizacion%20de%20raices%20III/Metodo_Newton_Raphson.py)
  - [Bairstow](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/Metodos%20de%20localizacion%20de%20raices%20III/Metodo_de_Bairstow.py)

- **Sistemas No Lineales**
  - [Broyden](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/SENL/Metodo_de_Broyden.py)
  - [Broyden II](./3.Solucion_Numerica_de_Sistemas_de_Ecuaciones_No_Lineales/SENL/Metodo_de_Broyden2.py)

---

### 4. [Cálculo de Valores y Vectores Propios](./4.Calculo_de_valores_y_vectores_propios)

- [Potencia Escalada](./4.Calculo_de_valores_y_vectores_propios/Metodo_de_la_Potencia_Escalada.py)
- [Potencia Inversa](./4.Calculo_de_valores_y_vectores_propios/Metodo_de_la_Potencia_Inversa.py)
- [Potencia Inversa Desplazada](./4.Calculo_de_valores_y_vectores_propios/Metodo_de_la_Potencia_Inversa_Desplazada.py)
- [Polinomios de Bernstein](./4.Calculo_de_valores_y_vectores_propios/Aproximacion_con_Polinomios_de_Bernstein.py)

---

### 5. [Aproximación Polinomial](./5.Aproximacion_Polinomial)

- **[Lagrange](./5.Aproximacion_Polinomial/Lagrange)**
  - [Ejemplos 1-3](./5.Aproximacion_Polinomial/Lagrange)

- **[Newton](./5.Aproximacion_Polinomial/Newton)**
  - [Ejemplos 1-5](./5.Aproximacion_Polinomial/Newton)
  - [Diferencia Progresiva](./5.Aproximacion_Polinomial/Newton/Diferencia_progresiva.py)
  - [Diferencia Regresiva](./5.Aproximacion_Polinomial/Newton/Diferencia_regresiva.py)

- **[Hermite](./5.Aproximacion_Polinomial/Hermite)**
  - [Hermite1 y 2](./5.Aproximacion_Polinomial/Hermite)

- **[Taylor](./5.Aproximacion_Polinomial/Taylor)**

- **[Interpolación Trigonométrica](./5.Aproximacion_Polinomial/InterpolacionTrigonometrica)**
  - [Fourier](./5.Aproximacion_Polinomial/InterpolacionTrigonometrica/Fourier)
  - [Trigonométrica directa](./5.Aproximacion_Polinomial/InterpolacionTrigonometrica)

- **[B-Splines](./5.Aproximacion_Polinomial/B-splines)**
  - [B-spline y Bezier](./5.Aproximacion_Polinomial/B-splines)
  - [Spline Cúbico + Rayleigh-Ritz](./5.Aproximacion_Polinomial/B-splines/spline_cubico/Rayleigh-Ritz)

---

