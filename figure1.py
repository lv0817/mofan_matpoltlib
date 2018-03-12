import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x+2
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,4))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.2,linestyle='--')

plt.xlim((-1,6))
plt.ylim((-2,6))
plt.xlabel('a')
plt.ylabel('b') 

new_ticks = np.linspace(-1,2,6)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1,1,5,6],
            [r'$a$',r'$b$',r'$c$',r'$d$',r'$e$'])


plt.show()
 
