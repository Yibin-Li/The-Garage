import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#different kind of plt functions(plots):
#'bar' : vertical bar plot
#'barh' : horizontal bar plot
#'hist' : histogram
#'box' : boxplot
#'pie' : pie plot
#'scatter' : scatter plot
#'hexbin' : hexbin plot

#different kind of line style or maker:
#'-'	solid line style
#'--'	dashed line style
#'-.'	dash-dot line style
#':'	dotted line style
#'.'	point marker
#','	pixel marker
#'o'	circle marker
#'v'	triangle_down marker
#'^'	triangle_up marker
#'<'	triangle_left marker
#'>'	triangle_right marker
#'1'	tri_down marker
#'2'	tri_up marker
#'3'	tri_left marker
#'4'	tri_right marker
#'s'	square marker
#'p'	pentagon marker
#'*'	star marker
#'h'	hexagon1 marker
#'H'	hexagon2 marker
#'+'	plus marker
#'x'	x marker
#'D'	diamond marker
#'d'	thin_diamond marker
#'|'	vline marker
#'_'	hline marker

# create a numpy array with 200 elements which uniformly distributed from -pi to pi 
x = np.linspace(-np.pi, np.pi, 200)
ax = plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), '-', color='Red')
plt.subplot(2, 1, 2, sharex=ax)
plt.plot(x, np.sin(2*x), color='Blue')
#plt.savefig('C:\\Users\\lyb\\Desktop\\subplot example.png')

plt.figure()
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
ax5.plot(x, np.cos(x), color='Yellow')
#set each lable to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)
#plt.savefig('C:\\Users\\lyb\\Desktop\\subplot example2.png')

plt.figure()
#create a histogram that counts each number's frequency
plt.hist([0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 9, 9, 9])
#plt.savefig('C:\\Users\\lyb\\Desktop\\histogram.png')

plt.figure()
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
ax = [ax1, ax2, ax3, ax4]
for n in range(len(ax)):
	sample_size = 10 ** n
	sample = np.random.normal(loc = 0, scale=1, size=sample_size)
	ax[n].hist(sample, bins=100)
	ax[n].set_title('n=%s' % sample_size)
#plt.savefig('C:\\Users\\lyb\\Desktop\\histogram2.png')

plt.figure()
#Customizing Location of Subplot Using GridSpec
import matplotlib.gridspec as gridspec
gspec = gridspec.GridSpec(3, 3) #similar to ax = plt.subplots(3, 3)
#9 plots are divided into 9 cell, and each cell has its own position 
#eg.(0, 0) is the upper leftward cell, (2, 2) is the lower rightward cell 
#every axis starts from 0, similar to a list
top_histogram = plt.subplot(gspec[0, 1:]) #combined the upper two subplots((0, 1) and (0, 2)) into a big cell 
side_histogram = plt.subplot(gspec[1:, 0]) #combined the leftward two subplots((1, 0) and (2, 0)) into a big cell
lower_right = plt.subplot(gspec[1:, 1:]) #combined the middle four subplots((1, 1), (1, 2), (2, 1), (2, 2)) into a big cell
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
lower_right.scatter(X, Y)
top_histogram.hist(X, bins=100)
side_histogram.hist(Y, bins=100, orientation='horizontal') #rotate the graph to horizon (similar to draw inverse function)
#plt.savefig('C:\\Users\\lyb\\Desktop\\gridspec.png')

plt.figure()
normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)
#create a dataframe that contains three different distributions
df = pd.DataFrame({'normal': normal_sample, 
                   'random': random_sample, 
                   'gamma': gamma_sample})
plt.boxplot(df['normal'])
#plt.savefig('C:\\Users\\lyb\\Desktop\\boxplot.png')

#the effect of whis attribute
plt.figure()
plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
#plt.savefig('C:\\Users\\lyb\\Desktop\\boxplot2.png')

plt.figure()
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
#loc attribute number
#'upper right'  : 1,
#'upper left'   : 2,
#'lower left'   : 3,
#'lower right'  : 4,
#'right'        : 5,
#'center left'  : 6,
#'center right' : 7,
#'lower center' : 8,
#'upper center' : 9,
#'center'       : 10
ax2.hist(df['gamma'], bins=100)
ax2.yaxis.tick_right()
#plt.savefig('C:\\Users\\lyb\\Desktop\\boxplot3.png')
ax2.margins(x=0.5) #set xaxis margin to 0.5
#plt.savefig('C:\\Users\\lyb\\Desktop\\boxplot4.png')

plt.figure()
x = np.random.random(size=10000)
y = np.random.normal(loc=0, scale=1, size=10000)
plt.hist2d(x, y, bins=100)
plt.colorbar()
#plt.savefig('C:\\Users\\lyb\\Desktop\\heatmap.png')
#plt.show()
print ('done')