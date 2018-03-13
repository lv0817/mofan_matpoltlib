import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)#加入一个三维坐标轴
#XYvalue
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)

Z = np.sin(R)


ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
# rstride row跨度 cstride coloum跨度
ax.contourf(X,Y,Z,zdir='x',cmap='rainbow',offset=-4)
# offset压到什么位置， zdir，从什么方向压
plt.show()