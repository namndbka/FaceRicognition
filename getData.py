# vẫn dùng cv2
import cv2
import  numpy as np
#để truy cập data từ sql thì import thêm thư viện này
import sqlite3
# os này để truy cập các đường dẫn trên máy
import os
# Hàm truy cập đến database, thêm mới hoặc update database
def insertOrUpdate(id, name):
    #do em để database ngay trong cùng file với bài code nên k cần đường dẫn dài
    conn = sqlite3.connect('data.db')
    query = "SELECT * FROM people WHERE ID="+ str(id)
    #lấy ra các bản ghi từ query
    cusror = conn.execute(query)
    # Biến kiểm tra id đã tồn tại chưa
    isRecordExist = 0
    #duyệt hàng trên bàn ghi
    for row in cusror:
        isRecordExist = 1
    #insert vào database
    if(isRecordExist == 0):
        query = "INSERT INTO people(ID, Name) VALUES("+str(id)+ ",'"+ str(name)+ "')"
    else :
        query = "UPDATE people SET Name='"+str(name)+"' WHERE ID="+ str(id)

    conn.execute(query)
    conn.commit()
    conn.close()

# như bài trước ạ, lode thư viện và dùng cam
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

#insert to db
id = input("Enter your ID: ")
name = input("Enter your Name: ")
insertOrUpdate(id, name)
# sử dụng một biến đếm
sampleNum = 0
# vẽ hình bao quanh khuôn mătj
while(True) :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        # tạo file chứa ảnh
        if not os.path.exists('dataSet'):
            os.makedirs('dataSet')
        #chụp từng frame
        sampleNum +=1
        cv2.imwrite('dataSet/User.'+str(id)+'.'+ str(sampleNum)+ '.jpg', gray[y: y+ h, x: x+ w])
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

        if sampleNum > 100 :
            break

cap.release()
cv2.destroyAllWindows()
