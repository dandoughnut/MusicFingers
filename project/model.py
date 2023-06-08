import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import test2 as t
import cv2

train_files = glob.glob("./fingers/train/*.png")
test_files = glob.glob("./fingers/test/*.png")

print(len(train_files), len(test_files))

train_files[0]

from PIL import Image
im = Image.open(train_files[0])
im2 = Image.open(test_files[1])
# plt.imshow(im)
plt.imshow(im2)
im_array = np.array(im)
im_array.shape
X_train = np.zeros((len(train_files), 128, 128))
Y_train = np.zeros((len(train_files), 12))
for i, trf in enumerate(train_files):
    im = Image.open(trf)
    X_train[i, :, :] = np.array(im)
    if trf[-5] == 'L':
        Y_train[i, int(trf[-6:-5])] = 1
    else:
        Y_train[i, int(trf[-6:-5])+6] = 1
X_test = np.zeros((len(test_files), 128, 128))
Y_test = np.zeros((len(test_files), 12))

print(X_test.shape)
for i, tsf in enumerate(test_files):
    if i == 0:
        print(tsf)
    im = Image.open(tsf)
    X_test[i, :, :] = np.array(im)
    if tsf[-5] == 'L':
        Y_test[i, int(tsf[-6:-5])] = 1
        print(tsf, int(tsf[-6:-5]))

    else:
        Y_test[i, int(tsf[-6:-5])+6] = 1
        print(tsf, int(tsf[-6:-5])+6)    
print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))
    
    