from matplotlib import pyplot as plt
import numpy as np

img = plt.imread("map.png")
plt.imshow(img)


height, width = img.shape[:2]
print(width, height)

