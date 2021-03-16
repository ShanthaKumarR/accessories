import cv2
path = 'frame/'

def dif_frame():
    capture = cv2.VideoCapture('cod_anne.mp4')
    i = 1
    j = 0
    while (capture.isOpened()):
    
        ret, frame = capture.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        if i <=6:
            if i == 4:
                cv2.imwrite(path + '{}.jpg'.format(j), frame)
                print(i)
             
            if i == 6:
               cv2.imwrite(path + '{}.jpg'.format(j), frame)
               print(i)
               i = 1
            i += 1
            j += 1
        
        if i >=6:
            i = 1
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
def all_frame(name):
    capture = cv2.VideoCapture(name)
    j = 0
    while (capture.isOpened()):
    
        ret, frame = capture.read()
        cv2.imshow('frame', frame)
        cv2.imwrite(path + '{}.jpg'.format(j), frame)
        
        j += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
 
all_frame(name = 'output_lab.avi')
