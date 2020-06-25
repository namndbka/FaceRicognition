#import các thư viện cần thiết
import cv2
import numpy as np
import os
import sqlite3
from PIL import Image

# training hinh anh nhan dien vs thu vien nhan dien khuon măt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
#đọc file training
recognizer.read('trainningData.yml')


# Lấy các thông tin thông qua id
def getProfile(id):
    conn = sqlite3.connect('data.db')
    query = "SELECT * FROM People WHERE ID=" + str(id)
    cursor = conn.execute(query)
    #biến profile để lưu giá trị mà mình tìm được từ database
    profile = None

    for row in cursor:
        profile = row

    conn.close()
    return profile

#sử dụng cam
cap = cv2.VideoCapture(0)
#font text
fontface= cv2.FONT_HERSHEY_SIMPLEX

#đọc dữ liệu từ cam và nhận diện khuôn mặt
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 2)
        #cắt ảnh và so sánh với tập dữ liệu trên máy
        #cắt ảnh xám
        roi_gray = gray[y:y + h, x: x + w]
        #gọi hàm nhận diện đang hiện trên cam, trả về một đoạn text nếu có tập dữ liệu
        id, confidence = recognizer.predict(roi_gray)
        #xử lý độ chính xác
        if confidence < 40:
            profile = getProfile(id)
            # nếu có dữ liệu thì đấy text là tên ra
            if profile != None:
                cv2.putText(frame, "" + str(profile[1]), (x + 10, y + h + 30), fontface, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknow", (x + 10, y + h + 30), fontface, 1, (0, 0, 255), 2)

        cv2.imshow('image', frame)
        if cv2.waitKey(1) == ord('q'):
            break;

cap.release()
cv2.destroyAllWindows()
