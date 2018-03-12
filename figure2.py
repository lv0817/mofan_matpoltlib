import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-1,6,50)
y1 = 2*x+2
y2 = x**2
y3 = x+1


plt.figure(num=3,figsize=(8,4))
l1, =plt.plot(x,y2,label='first')
l2, =plt.plot(x,y1,color='red',linewidth=1.2,linestyle='--',label='second')
plt.plot(x,y3,label='third')
plt.xlim((-1,6))
plt.ylim((-2,6))
plt.xlabel('first')
plt.ylabel('second') 

new_ticks = np.linspace(-1,6,12)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1,1,5,6],
            [r'$a$',r'$b$',r'$c$',r'$d$',r'$e$'])

#plt.legend(),labels替代了原来的label
plt.legend(handles=[l1,l2,],labels=['aaa','bbb'],loc='best')

plt.show()
 
