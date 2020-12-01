import cv2

cap = cv2.VideoCapture(0)

#fps = int(cap.get(5))
cap.set(cv2.CAP_PROP_FPS, 20)
cap.set(cv2.CAP_PROP_POS_MSEC, 0.25*1000)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Fish_30_vid_d.avi',fourcc, 7, (640,480))

while(cap.isOpened()):

    ret,frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    

    cv2.waitKey(250)
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#############################################################################
######################Low frame rate video################################### 




 
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 1, (640,480))

# import time

# capture = cv2.VideoCapture(0)
# capture.set(3, 640)
# capture.set(4, 480)
# img_counter = 0
# frame_set = []
# start_time = time.time()

# while True:
    # ret, frame = capture.read()
    # #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break
    # if time.time() - start_time >= 1: #<---- Check if 5 sec passed
        # #img_name = "opencv_frame_{}.png".format(img_counter)
        # #cv2.imwrite(img_name, frame)
        # out.write(frame)
        # #print("{} written!".format(img_counter))
        # start_time = time.time()
    # img_counter += 1
    
    
    
    
    
########################################frame rate of the video########################

import time


capture = cv2.VideoCapture('cod_fast_frame.mp4')

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 5, (width,height))



print(fps)
while (capture.isOpened()):
    ret, frame = capture.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    
