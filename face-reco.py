import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
    _, img = webcam.read()
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert colour image to gray image

    faces = face_cascade.detectMultiScale(gray_img, 1.5, 4) 
    # detect if face is present or not
    # return four values(x,y,w,h)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Face Detection", img)


    key = cv2.waitKey(10) # wait for 10 miliseconds
    if key == 27: #Escape key for break the loop (stop the web cam)
        break

webcam.release()
cv2.destroyAllWindows()

