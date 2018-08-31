#Jorge Dettle Meza Dominguez
#29/08/18
#grafica de dos funciones
import matplotlib.pyplot as plt
import numpy as np
def f1(x):
		return 2*(x**2)+5*x-2

def f2(x):
        return 4*x+1

x =np.arange(-10, 15, 0.1)

plt.plot(x, [f1(i) for i in x], "bo", label="f1")
plt.plot(x, [f2(i) for i in x], "go", label="f2")

plt.axhline(0, color="black")
plt.axvline(0, color="black")
 

plt.legend(loc="upper right")
plt.savefig("output.png")

plt.show()