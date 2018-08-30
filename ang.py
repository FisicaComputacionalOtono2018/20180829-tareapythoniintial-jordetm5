#jorge Dettle Meza Dominguez
#29/18
#calcular angulos
import math

def magnitud(x) :
    p=0
    for i in range (0,3) :
        p=p+(x[i]**2)
    return math.sqrt(p)


def f(x) :
    m=magnitud(x)
    an=[]
    for i in range (0,3):
        an.append(math.acos(x[i]/m))
    return an

a= []
for i in range (0,3):
   a.append(int(input("dame el valor de la componente de A: ")))

print(f(a))

