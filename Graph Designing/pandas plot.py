import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
purchase_1 = pd.Series({'bgn': 5, 'ugb': 2, 'uhn': 9})
purchase_2 = pd.Series({'bgn': 999, 'ugb': 234, 'uhn': 176})
purchase_3 = pd.Series({'bgn': 99, 'ugb': 24, 'uhn': 16})
new = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['store1', 'store2', 'store3'])
new.plot()
plt.savefig('C:\\Users\\lyb\\Desktop\\pandas plot.png')

plt.figure()
new.plot('bgn', 'ugb', kind = 'scatter')
plt.savefig('C:\\Users\\lyb\\Desktop\\pandas plot2.png')
#kind :
#'line' : line plot (default)
#'bar' : vertical bar plot
#'barh' : horizontal bar plot
#'hist' : histogram
#'box' : boxplot
#'kde' : Kernel Density Estimation plot
#'density' : same as 'kde'
#'area' : area plot
#'pie' : pie plot
#'scatter' : scatter plot
#'hexbin' : hexbin plot

plt.figure()
# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
ax = new.plot.scatter('bgn', 'uhn',c='ugb', s=new['ugb'], colormap='viridis')
#ax.set_aspect('equal') #set xaxis and yaxis have the same range of interval
plt.savefig('C:\\Users\\lyb\\Desktop\\pandas plot3.png')

plt.figure()
new.plot.box()
plt.savefig('C:\\Users\\lyb\\Desktop\\pandas plot4.png')

plt.figure()
new.plot.hist(alpha = 0.9)
plt.savefig('C:\\Users\\lyb\\Desktop\\pandas plot5.png')

plt.figure()
v1 = pd.Series(np.random.normal(0, 10, 1000))
v2 = pd.Series(2*v1 + np.random.normal(60, 15, 1000))
plt.hist(v1, alpha=0.7, bins=np.arange(-50,150,5), label='v1')
plt.hist(v2, alpha=0.7, bins=np.arange(-50,150,5), label='v2')
plt.legend()
plt.savefig('C:\\Users\\lyb\\Desktop\\pandas plot6.png')

#seaborn functionality
#plt.figure()
# we can pass keyword arguments for each individual component of the plot
#sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'})
#plt.savefig('C:\\Users\\lyb\\Desktop\\seaborn plot.png')

#plt.figure()
#sns.jointplot(v1, v2, alpha=0.4)
#plt.savefig('C:\\Users\\lyb\\Desktop\\seaborn plot2.png')

#seaborn hex plot
#plt.figure()
#sns.jointplot(v1, v2, kind='hex')
#plt.savefig('C:\\Users\\lyb\\Desktop\\seaborn plot3.png')
#plt.show()
print ('done')

