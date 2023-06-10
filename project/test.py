import cv2
import mediapipe as mp
import sys
from random import randint
import time

# class for hand detection and tracking
class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def handsFinder(self,image,draw=True):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
    
    def positionFinder(self,image, handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(Hand.landmark):
                h,w,c = image.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])
            if draw:
                cv2.circle(image,(cx,cy), 15 , (255,0,255), cv2.FILLED)

        return lmlist

def main():
    how_many = 0
    cap = cv2.VideoCapture(0) # Replace 0 with the video path to use a pre-recorded video

    # set the webcam resolution to fit our model
    # cap.set(cv2.CV_CAP_PROP_FRAME_WIDTH, 280)
    # cap.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 280)

    tracker = handTracker()

    while True:
        success, frame = cap.read()

        # set the frame to gray scale or RGB (not sure which one works better for us)
        # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # pass frame_gray or frame_rgb into out CNN model for hand gesture recognition
        # TODO: pass frame into model

        
        frame = tracker.handsFinder(frame) # passing in frame bc handsFinder converts BGR images to RGB
        lmlist = tracker.positionFinder(frame)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.resize(frame_gray, (128, 128), interpolation = cv2.INTER_AREA)

        if len(lmlist) != 0:
            
            # lmlist contains [id, cx, cy]
            x = lmlist[0][1] # get the x of the first landmark
            y = lmlist[0][2] # get the y of the first landmark
            print (x, y)
            # use x and y to map to musical notes
            # TODO: pass x and y into music-generating function

        cv2.imshow('MusicFingers', frame_gray)
        # if how_many < 10:
            # time.sleep(0.5)
            # cv2.imwrite(str(how_many)+'.png', frame_gray)
            # how_many += 1
        if cv2.waitKey(1) & 0XFF == 27: # esc key
            break # if esc key is pressed, the video window will be closed





        






if __name__ == "__main__":
    main()