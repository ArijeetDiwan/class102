
import cv2

def take_snapshot():

    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frame while the camara is on 
        ret,frame=videoCaptureObject.read()
        print(ret)
        #cv2.imwrite() is use to save the image to any storage device
        #cv2.imwrite("./picture.jpg",frame)
        cv2.imwrite("C:/Users/dell/Downloads/picture.jpg",frame)
        result=False

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()        

