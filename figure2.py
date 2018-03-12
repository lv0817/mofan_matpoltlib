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

#gca ='get current axis'
ax = plt.gca()
#设置边框颜色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('red')
#设置那两条边作为坐标轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#设置坐标轴的位置
ax.spines['bottom'].set_position(('data',0))#data,outward,axes(轴的百分比)
ax.spines['left'].set_position(('data',0))


plt.show()
 
