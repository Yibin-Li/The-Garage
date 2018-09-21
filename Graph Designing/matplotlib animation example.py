import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

n = 100
x = np.random.randn(n)

# create the function that will do the plotting, where curr is the current frame
def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == 100:	
        anim.event_source.stop() #stop the animation
        plt.figure()
    plt.cla()
    bins = np.arange(-4, 4, 0.5)
    plt.hist(x[:curr], bins=bins)
    plt.axis([-4,4,0,30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr), [3,27])
    
	
fig = plt.figure()
anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()
print ('done')