import cv2
import dropbox
import time
import random

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        result = False

    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadImg(imageName):
    access_token = imageName
    file = image_counter
    file_from = file
    file_to = "/Users/bryancastro/desktop/Coding/PythonTest-4"
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read().file_to)

take_snapshot()
uploadImg()