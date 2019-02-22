import numpy as np
import cv2
"""
file_name = input("File name:")
myArray = np.load(open(file_name, 'rb'))
print(myArray)
"""

pic = cv2.imread("./blur/4variationblur0.png")

print(pic.shape)
newx, newy = pic.shape[1]/4,pic.shape[0]/4
new_pic = cv2.resize(pic, (int(newx), int(newy)))
cv2.imshow("original pic", pic)
cv2.imshow("modified pic", new_pic)

cv2.waitKey(0)
