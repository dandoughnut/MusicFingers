
# importing OpenCV library
import cv2
import time
from PIL import Image
import matplotlib.pyplot as plt
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam = cv2.VideoCapture(0)
# im = Image.open('./3.png')
# im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# plt.imshow(im_gray)

# reading the input using the camera

  
# If image will detected without any error, 
# show result
current = 0

for i in range(15):
    result, image = cam.read()
    if result:
        # showing result, it take frame name and image 
        # output
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("GeeksForGeeks", image)
        time.sleep(0.5)
        # saving image in local storage
        image_gray = cv2.resize(image_gray, (128, 128), interpolation=cv2.INTER_AREA)
        cv2.imwrite(str(current) + ".png", image_gray)
        current += 1
        print(image_gray.size)
    
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
cv2.waitKey(0)
cv2.destroyWindow("GeeksForGeeks")
print("end")
