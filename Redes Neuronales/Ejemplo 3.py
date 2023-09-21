
'''
from math import exp
import sympy as sp
from sympy.utilities import lambdify

x11=0
x12=0
x21=0
x22=1
x31=1
x32=0
x41=1
x42=1
y1=1
y2=1
y3=1
y4=0
n=4

w1, w2, b= sp.symbols('w1 w2 b')

C = (1/(2*n))*(((1 / (1 + sp.exp(-(w1*x11+w2*x12+b))))-y1)**2+((1 / (1 + sp.exp(-(w1*x21+w2*x22+b))))-y2)**2+((1 / (1 + sp.exp(-(w1*x31+w2*x32+b))))-y3)**2+((1 / (1 + sp.exp(-(w1*x41+w2*x42+b))))-y4)**2)
C_eval = lambdify((w1,w2,b), C, "numpy")

derivada_w1 = sp.diff(C, w1)
derivada_w1_eval = lambdify((w1,w2,b), derivada_w1, "numpy")
derivada_w2 = sp.diff(C, w2)
derivada_w2_eval = lambdify((w1,w2,b), derivada_w2, "numpy")
derivada_b = sp.diff(C, b)
derivada_b_eval = lambdify((w1,w2,b), derivada_b, "numpy")
W1 = -1
W2=-1
B=1
eta=0.001

List=[]
c=0
P=1
while C_eval(W1,W2,B)>0.01 :
    if c% P == 0:
        print(c)
        List.append(C_eval(W1,W2,B))
        P=P*10
    W1=W1-eta*(derivada_w1_eval(W1,W2,B))
    W2=W2-eta*(derivada_w2_eval(W1,W2,B))
    B=B-eta*(derivada_b_eval(W1,W2,B))
    c=c+1
print(List)  
print(c)  

   


print(C_eval(W1,W2,B))    
print(W1,W2,B)
print((1 / (1 + exp(-(W1*x11+W2*x12+B)))))
print((1 / (1 + exp(-(W1*x21+W2*x22+B)))))
print((1 / (1 + exp(-(W1*x31+W2*x32+B)))))
print((1 / (1 + exp(-(W1*x41+W2*x42+B)))))
'''

import matplotlib.pyplot as plt

# Datos
x = [0, 10, 100, 1000, 10000, 100000, 588039]
y = [0.08058237203212831, 0.08053684779395877, 0.08013086796426971, 0.07642348344611484, 0.05977434683869173, 0.03525470740933883, 0.009999989551141186]

# Crear el gráfico de líneas
plt.plot(x, y, label='Datos de Error', color='blue', marker='o', linestyle='-')

# Etiquetas de los ejes
plt.xlabel('Iteraciones')
plt.ylabel('Valor de la función de error')

# Título del gráfico
plt.title('Gráfico de Error vs. Iteraciones con Líneas Rectas')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()

