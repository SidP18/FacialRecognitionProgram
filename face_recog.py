# need to start by installing opencv from the command prompt using pip install opencv-python
# download haarcascade_frontalface_default.xml file from github online using opencv documentation
# import from cv2 to get the opencv
import cv2

# load the cascade file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# uses the image that is found within the project folder
img = cv2.imread('test.jpg.jpg')

# converts any image to greyscale so that it is easier for the program to recognize faces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    # draws a rectangle around the face that the program detects
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

# displays the image with the faces detected and the rectangle(s)
cv2.imshow('img', img)
# in case the user presses a key then the image stops showing
cv2.waitKey()

cv2.imwrite("face_detected.jpg", img)

# to run the program, the user can write 'python face_recog.py'
