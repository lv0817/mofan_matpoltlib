import matplotlib.pyplot as plt 
import numpy as np 

def f(x,y):
    # the hight function
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y =np.meshgrid(x,y)

# use plt.contourf to filling contours
#XY and value for (XY)point
plt.contourf(X,Y,f(X,Y),8,alpha=0.7,cmap=plt.cm.hot)#contour的图
# use plt.contour to add contour lines
C= plt.contour(X,Y,f(X,Y),8,colors='black')
# 8 代表等高线颜色分了多少部分，0-2部分，8-10部分
# adding label
plt.clabel(C,inline=True,fontsize=10)#inline表示是否在线里

plt.xticks(())
plt.yticks(())
plt.show()