import cv2
import dropbox
import time
import random

#print(time.time())
#print(random.randint(0,9))

start_time=time.time()


def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frame while the camara is on 
        ret,frame=videoCaptureObject.read()
        print(ret)
        #cv2.imwrite() is use to save the image to any storage device
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        #cv2.imwrite("C:/Users/dell/Downloads/picture.jpg",frame)
        start_time=time.time
        result=False
        
    return img_name
    print("snapshot taken")
    #release the camara
    videoCaptureObject.release()
    #close all the windows  
    cv2.destroyAllWindows()

#take_snapshot()    
    
def upload_file(img_name):
    access_token="g-p5Q8UE7SMAAAAAAAAAATRI3f2wBCR_VxvDbHBdZd54dRvMS-_481jUC5r2IbmG"
    file=img_name
    file_from=file
    file_to="/Python_Arijeet/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()
