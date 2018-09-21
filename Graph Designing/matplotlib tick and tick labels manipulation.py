import matplotlib.pyplot as plt
tempy_max = [259, 273, 264, 284, 252, 277, 239, 251, 256, 244, 273, 270, 265, 
260, 284, 280, 263, 264, 267, 262, 284, 276, 290, 276, 292, 293, 282, 292, 
283, 266, 337, 305, 307, 305, 317, 301, 326, 309, 294, 311, 338, 334, 343, 
339, 338, 326, 341, 336, 354, 356, 373, 345, 352, 337, 354, 356, 398, 345, 
370, 360, 363, 377, 392, 386, 380, 385, 382, 382, 389, 383, 390, 386, 409, 
379, 378, 384, 383, 378, 407, 388, 362, 360, 369, 350, 358, 383, 367, 368, 
357, 366, 329, 320, 332, 324, 328, 322, 318, 326, 334, 327, 308, 292, 303, 
308, 314, 279, 318, 284, 298, 301, 266, 283, 268, 270, 264, 274, 274, 264, 
256, 266]
tempx_max2015 = [7, 14, 30, 32, 41, 54, 61, 71, 91, 102, 111]
tempy_max2015 = [249, 261, 274, 313, 346, 342, 385, 391, 330, 303, 280]

tempy_min = [-57, -69, -33, -61, -59, -76, -88, -73, -67, -67, -51, -87, -51, 
-58, -37, -53, -56, -96, -88, -91, -46, -50, -26, -19, -25, -28, -70, -43, 
-39, -67, 31, 31, 6, 11, 16, -12, 11, -10, 13, 22, 85, 91, 100, 37, 92, 66, 
89, 90, 84, 93, 159, 121, 124, 110, 133, 138, 89, 113, 141, 123, 193, 146, 
155, 184, 171, 185, 132, 149, 172, 155, 171, 162, 180, 147, 163, 210, 158, 
191, 200, 157, 101, 130, 105, 117, 124, 100, 135, 137, 142, 143, 72, 98, 
97, 80, 94, 52, 96, 77, 98, 59, 12, 34, 11, -1, 28, 16, 27, -1, -22, 13, 
-69, -46, -40, -38, -69, -81, -63, -70, -57, -56]
tempx_min2015 = [3, 11, 23, 31, 51, 61, 71, 82, 91, 101]
tempy_min2015 = [-53, -72, -43, -3, 130, 151, 159, 128, 57, 9]

tempx = [x+1 for x in range(120)]
tempy_max = [float(i / 10) for i in tempy_max]
tempy_min = [float(i / 10) for i in tempy_min]
tempy_max2015 = [float(i / 10) for i in tempy_max2015]
tempy_min2015 = [float(i / 10) for i in tempy_min2015]

plt.figure()
plt.plot(tempx, tempy_max, '-', color='Red', alpha=0.5)
plt.plot(tempx, tempy_min, '-', color='Blue', alpha=0.5)
plt.gca().fill_between(tempx, tempy_max, tempy_min, alpha=0.25)
plt.plot(tempx_max2015, tempy_max2015, '.', color='Red')
plt.plot(tempx_min2015, tempy_min2015, '.', color='Blue')
ax = plt.gca()
ax.axis([0, 121, -20, 45])
#ax.xaxis.set_ticks(x_tick)

#customize each ticks and ticks' label
x_tick_label = ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
x_tick = [i * 10 for i in range(13)]
y_tick_label = ['', '-20℃', '-10℃', '0℃', '10℃', '20℃', '30℃', '40℃']
y_tick = [i * 10 - 30 for i in range(8)]
plt.xticks(x_tick, x_tick_label, fontsize=10)
plt.yticks(y_tick, y_tick_label, size='small')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Extreme 2015 temperature against 2005-2014', fontsize=12)
plt.legend(['High(2005-2014)', 'Low(2005-2014)', 'High(2015)', 'Low(2015)', 'Expected Temperature Gap'])
ax = plt.gca()
ax.yaxis.tick_right()
plt.show()