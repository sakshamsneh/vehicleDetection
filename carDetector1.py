import cv2
cap = cv2.VideoCapture('C://Users//SAKSHIM//Documents//python//opencv//abc3.mp4')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter("C://Users//SAKSHIM//Documents//python//opencv//abc2.avi", fourcc, 25, size)
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('C://Users//SAKSHIM//Documents//python//opencv//cars.xml')
# loop runs if capturing has been initialized.
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver)  < 3 :
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
else :
    fps = cap.get(cv2.CAP_PROP_FPS)
intTimeToNextFrame=int(1000.0/fps)-12 # '-12' estimation of time for processing
while True:
    (grabbed,frame) = cap.read()
    grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(grayvideo, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),1)
    video.write(frame)
    cv2.imshow("video",frame)
    if cv2.waitKey(intTimeToNextFrame)== ord('q'):
        break
cap.release()
video.release()
cv2.destroyAllWindows()
