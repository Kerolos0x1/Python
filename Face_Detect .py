import cv2
import os

#Insert your Image Name with Extension like: ex.png
image = ""

opencv_data_dir = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
face_detect = cv2.CascadeClassifier(opencv_data_dir)
read_image = cv2.imread(image)

#Try to Adjust your Diminsion
read_image = cv2.resize(read_image,(300,500))

face = face_detect.detectMultiScale(read_image)
num_faces = f"{len(face)} Faces Detection"
for (x,y,w,h) in face:
    cv2.rectangle(read_image,(x,y),(x+w,y+w),(0,255,0),1)
    
cv2.putText(read_image,num_faces,(20,20),1,1.1,(0,255,0),1,cv2.FONT_HERSHEY_COMPLEX)
cv2.imshow("Image",read_image)
cv2.waitKey(0)