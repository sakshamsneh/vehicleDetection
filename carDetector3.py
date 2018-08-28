import cv2
import imutils
import time
import matplotlib.pyplot as plt
import pyrebase

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password()
user = auth.refresh(user['refreshToken'])
db = firebase.database()

backsub = cv2.createBackgroundSubtractorMOG2()
cap = cv2.VideoCapture("C://Users//SAKSHIM//Documents//python//opencv/q.mp4") 
i = j= c= 0
ret, frame = cap.read()
im=plt.imshow(frame, interpolation='none')
plt.ion()
minArea=1
while True:
    ret, frame = cap.read()
    fgmask = backsub.apply(frame, None, 0.01)  
    if fgmask is None:
        break                                    
    erode=cv2.erode(fgmask,None,iterations=2)     
    moments=cv2.moments(erode,True)              
    area=moments['m00']
    cv2.line(frame,(150,250),(297,249),(255,0,0),5)
    cv2.line(frame,(552,299),(461,335),(255,0,0),5)

    if area >=minArea:
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        
        if(c==0):
            if x>150 and x<160 and y>250 and y<296 or (x>240 and x<249 and y>249 and y<297):
                i=i+1
                cv2.line(frame,(150,250),(297,249),(0,255,0),5)
                c=4
                data={"time": time.time(), "count_l":i}
                res=db.child("place").child("1234").push(data, user['idToken'])
                print(i)
            
            elif x>552 and x<558 and y>299 and y<355 or( x>461 and x<470 and y>325 and y<335):
                j=j+1
                cv2.line(frame,(552,299),(461,335),(0,255,0),5)
                c=4
                data={"time": time.time(), "count_r":j}
                res=db.child("place").child("1234").push(data, user['idToken'])
                print(j)
        else:
            c=c-1  
            continue  
        
            
    cv2.putText(frame,'Left Lane: %r' %i, (10,30), cv2.FONT_HERSHEY_COMPLEX,
                        1, (0, 255, 0), 2)
    cv2.putText(frame,'Right Lane: %r' %j, (380,30), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 0), 2)
        
    key = cv2.waitKey(50)
    
    if  key== ord('p'):
        while True:
            key2=cv2.waitKey(0)
            if key2==ord('p'):
                break
    im.set_data(frame)
    plt.pause(0.01)
#    cv2.imshow("Traffic Video Feed", frame)
#    cv2.imshow("Foreground Mask", fgmask)
    if key == ord('q'):
            break

plt.ioff()
plt.show(False)
cv2.destroyAllWindows()  
