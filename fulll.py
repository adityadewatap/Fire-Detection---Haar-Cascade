#fileasli
import cv2
import numpy as np
import smtplib
import threading
from playsound import playsound


def send_mail_function():

    recipientEmail = "adityadewatap@gmail.com"
    recipientEmail = recipientEmail.lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("mer4h.apel@gmail.com", 'Kanaka250697')
        server.sendmail('mer4h.apel@gmail.com', recipientEmail, "Ada Api!!")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
    	print(e)

dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap=cv2.VideoCapture(camSet)

fire_cascade = cv2.CascadeClassifier('/home/skripsi/Desktop/pyPro/firedetectsound/fire_detection.xml')


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("fire is detected")
        playsound('/home/skripsi/Desktop/pyPro/alarm.mp3')
        threading.Thread(target=send_mail_function).start()
        
    cv2.imshow('Deteksi Api', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break