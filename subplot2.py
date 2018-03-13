import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec

# method 1 subplot2grid

plt.figure()
ax1 = plt.subplot2grid((3,3),(0,1),colspan=2,rowspan=1)#(0,1)为起始位置
ax1.plot([1,2],[2,3])
ax1.set_title('ax1_title')
ax1.set_xlabel('ax1_x_label')

ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,)#(0,1)为起始位置
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2,)
ax4 = plt.subplot2grid((3,3),(2,0),colspan=2,)






# method 2 gridspec

# method 3 easy to define structure


plt.tight_layout()
plt.show()