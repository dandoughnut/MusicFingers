import numpy as np
from PIL import Image
import cv2

# Creates a random image 100*100 pixels
# im = Image.open('./ourData/9.png')
sample = Image.open('./sample.png')
im = Image.open('./ourData/6.png')
im_array = np.array(im)
maxim = np.max(sample)
minim = np.min(sample)
print(maxim, minim)
im_array = np.array(maxim - im_array)
# mat = np.random.random((100,100))

# Creates PIL image
img = Image.fromarray(im_array, 'L')
img = img.save('r6.png')

img.show()