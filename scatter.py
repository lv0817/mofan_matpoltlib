import matplotlib.pyplot as plt
import numpy as np  

n=1024
X = np.random.normal(0,1,n)#正太分布
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)#颜色显示

#plt.scatter(X,Y,s=70,c=T,alpha=0.5)#s-size c-color cmap-default,alpha透明度
plt.scatter(np.arange(10),np.arange(10))
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

plt.xticks(())#xticks为空
plt.yticks(([-1,0,1]))#xticks为空

plt.show()




