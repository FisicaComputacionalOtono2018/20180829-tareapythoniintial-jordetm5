#Jorge Dettle Meza Dominguez
#29/08/2018
#producto cruz

c1=0
c2=0
c3=0

a= []
for i in range (0,3):
   a.append(int(input("dame el valor de la componente de A: ")))

b = []
for i in range (0,3):
    b.append(int(input("dame el valor de la componente de B: ")))


c1= (a[1]*b[2]-a[2]*b[1])
c2= (a[2]*b[0]-a[0]*b[2])
c3 = (a[0]*b[1]-a[1]*b[0])

print("el producto vectorial de A y B es: (",c1,c2,c3,")")
