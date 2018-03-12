import matplotlib.pyplot as plt 
import numpy as np 

n =12 
X = np.arange(n)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='blue',edgecolor='gray')
plt.bar(X,-Y2,facecolor='red',edgecolor='white')

for x,y in zip(X,Y1):
    # ha  horizontal aligment对齐方式
    plt.text(x,y+0.01,'%.2f' % y,ha='center',va='bottom')

for x,y in zip(X,Y2):
        # ha  horizontal aligment对齐方式
    plt.text(x,-y-0.1,'%.2f' % y,ha='center',va='top')




plt.xlim(-5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()