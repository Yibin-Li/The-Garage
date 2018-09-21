print (0)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 4, 5, 6, 7, 8, 9, 10]
z = range(len([2, 3, 4, 5, 6, 7, 8, 9, 10]))
plt.plot(3, 2, '.', 5, 6, '.')
#plt.savefig('C:\\Users\\lyb\\Desktop\\MyFig.png')
#plt.show()
print (1)

plt.figure() #open a new figure, and keep previous figure
colors = ['red']*(len(x)-1)
colors.append('green')
plt.scatter(y, x, s=10, color=colors)
#plt.savefig('C:\\Users\\lyb\\Desktop\\MyFig2.png')
#plt.show() 
print (2)

#plt.clf() #clear current figure, and draw a new figure
plt.figure() 
plt.xlabel('X legend')
plt.ylabel('Y legeng')
plt.title('HYGBBBBB')
d = np.arange('2017-01-01', '2017-01-10', dtype='datetime64[D]')
d = list(map(pd.to_datetime, d))
plt.plot(d, x, '-o')
xaxis = plt.gca().xaxis
for p in xaxis.get_ticklabels():
	p.set_rotation(45)
plt.subplots_adjust(bottom=0.25)
#plt.savefig('C:\\Users\\lyb\\Desktop\\MyFig3.png')
#plt.show()
print (3)

#plt.clf()
plt.figure()
m = []
for l in x:
	m.append(l - 0.15)
plt.bar(m, y, width = 0.3)
b = []
w = []
for i in x:
	w.append(i**2)
for l in x:
	b.append(l + 0.15)
plt.bar(b, w, width=0.3, color='red')
plt.xlabel('dddd')
plt.ylabel('bvdc')
plt.title('bqwerrt')
plt.legend(['normal', 'quardratic'])
#ax = plt.gca()
#ax.axis([])
#plt.savefig('C:\\Users\\lyb\\Desktop\\MyFig4.png')
plt.show()
print ('done')