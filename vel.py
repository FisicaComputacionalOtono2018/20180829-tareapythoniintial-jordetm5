#Jorge Dettle Meza Dominguez
#29/08/2018
#velocidad
count=1
stringinput = input("dame las distancias y los tiempos en el formato(m1,t1) use o,o para finalizar")

print(stringinput)

stringinput = stringinput.replace(')(',' ').replace(')','').replace(',',' ') 
    
print(stringinput) 

for i in stringinput:
     print(i)
     if count%2!=0:
         i=i/60
     
print(stringinput)

