import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x+2
y2 = x**2
plt.plot(x,y)
plt.plot(x,y2)
plt.show()
 