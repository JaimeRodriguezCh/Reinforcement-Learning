from math import exp
import sympy as sp
from sympy.utilities import lambdify
import matplotlib.pyplot as plt
## Conjunto T y parametros
x11, x12, x21, x22, x31, x32, x41, x42, y1, y2, y3, y4, n, W1, W2, B, eta, list, c, P = 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 4, -1, -1, 1, 0.001, [], 0, 1

# Definicion de Funcion C
w1, w2, b= sp.symbols('w1 w2 b')
C = (1/(2*n))*(((1 / (1 + sp.exp(-(w1*x11+w2*x12+b))))-y1)**2+((1 / (1 + sp.exp(-(w1*x21+w2*x22+b))))-y2)**2+((1 / (1 + sp.exp(-(w1*x31+w2*x32+b))))-y3)**2+((1 / (1 + sp.exp(-(w1*x41+w2*x42+b))))-y4)**2)
C_eval = lambdify((w1,w2,b), C, "numpy")

#Definicion de sus derivadas
derivada_w1 = sp.diff(C, w1)
derivada_w1_eval = lambdify((w1,w2,b), derivada_w1, "numpy")
derivada_w2 = sp.diff(C, w2)
derivada_w2_eval = lambdify((w1,w2,b), derivada_w2, "numpy")
derivada_b = sp.diff(C, b)
derivada_b_eval = lambdify((w1,w2,b), derivada_b, "numpy")


# Algoritmo de descenso del gradiente con criterio de parada C_T(w,b)<0.01
while C_eval(W1,W2,B)>0.01 :
    if c%P==0:
        list.append(C_eval(W1,W2,B))
        P=10*P
        print(c)
    W1=W1-eta*(derivada_w1_eval(W1,W2,B))
    W2=W2-eta*(derivada_w2_eval(W1,W2,B))
    B=B-eta*(derivada_b_eval(W1,W2,B))
    c=c+1

list.append(C_eval(W1,W2,B))
#Resultados
print(C_eval(W1,W2,B))    
print(W1,W2,B)
print((1 / (1 + exp(-(W1*x11+W2*x12+B)))))
print((1 / (1 + exp(-(W1*x21+W2*x22+B)))))
print((1 / (1 + exp(-(W1*x31+W2*x32+B)))))
print((1 / (1 + exp(-(W1*x41+W2*x42+B)))))



# Grafico ilustrativo que muestra como la función de error decrementa a medida que pasan iteraciones.
x = [0, 10, 100, 1000, 10000, 100000, 588039]
y = list

# Crear el gráfico de líneas
plt.plot(x, y, label='Datos de Error', color='blue', marker='o', linestyle='-')

# Etiquetas de los ejes
plt.xlabel('Iteraciones')
plt.ylabel('Valor de la función de error')

# Título del gráfico
plt.title('Gráfico de Error vs. Iteraciones')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()

