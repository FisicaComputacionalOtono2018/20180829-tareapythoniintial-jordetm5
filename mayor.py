
#jorge Dettle Meza Dominguez
#29/08/2018
#imprimir el mayor



m=[]
for i in range (0,4):
	m.append(int(input("dame el numero: ")))

for i in range(0, len(m)):
	for i in range (0,len(m)):
                
		if i<len(m)-1:
			if m[i]>m[i+1]:

				e=m[i]
				m[i]=m[i+1]
				m[i+1]=e

print(m[3])


