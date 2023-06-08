
# import the opencv library
import cv2
import time
import numpy as np

  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
# while(True):
for i in range(5):      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    time.sleep(0.5)
    # Display the resulting frame
    # cv2.imshow('Model', frame)
    #
    input_array = np.zeros((1, 128, 128))
    #
    input_frame = cv2.resize(frame, (128, 128), interpolation = cv2.INTER_AREA)
    frame_array = np.array(input_frame)
    print(frame_array.shape)
    cv2.imshow('Model', input_frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()