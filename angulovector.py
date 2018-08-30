#Jorge Dettle Meza Dominguez
#29/08/2018
#funcion para obtener el angulo entre dos vectores
import numpy as np
import math

def magnitud(x) :
    p=0
    for i in range (0,3) :
        p=p+(x[i]**2)
    return math.sqrt(p)
pr=0
r=0  

a= []
for i in range (0,3):
   a.append(int(input("dame el valor de la componente de A: ")))

b = []
for i in range (0,3):
    b.append(int(input("dame el valor de la componente de B: ")))





#producto punto
for i in range(0,3):
	pr = pr + (a[i]*b[i])
	 
r = math.acos(pr/(magnitud(a)*magnitud(b)))

print(r)