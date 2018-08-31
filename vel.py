#Jorge Dettle Meza Dominguez
#29/08/2018
#velocidad



def c(x):
    for i in range(0, len(x)):
        x[i]=x[i]*60
    return x
def v(x):
    
    for i in range (0, (len(x)-1)):
        x[i]=(1500.0/x[i])

    return x

def promedio(x):
	d=0
	s=0.0
	for i in range(0, len(x)):
		d=d+1
		s=s+x[i]
		if x[i] == 0:
			break
	return (s/(d-1))

count=1

stringinput = input("dame los tiempos en minutos y segundos en el formato(m1,s1) use (0,0) para finalizar  ")

stringinput = stringinput.replace(')(',' ').replace(')','').replace(',',' ').replace('(','')
    
m=[]
for i in stringinput:
    if i!=' ':
        m.append(int(i))
            
     
o=[]
p=[]
for i in m :
    if count%2== 0:
        o.append(i)
    else :
        p.append(i)
    count=count+1

n=c(p)
q=[]

 
for i in range(0, len(n)):
	q.append(n[i]+o[i])

r=v(q)
print(r)

print(promedio(r))
