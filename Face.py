# import các thư viện cần thiết
import cv2
# numpy giúp hỗ trợ thao tác với mảng array nhanh hơn, tối ưu hóa, truy xuất
import numpy as np

# Sử dụng opencv để lấy khuôn mặt trên webcam
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Truy cập camera
cap = cv2.VideoCapture(0)

# vòng while để hiển thị liên tục
while(True):
    # lấy dữ liệu từ webcam, ret trả về true nếu truy cập thành công, frame là data
    ret, frame = cap.read()
    # chuyển ảnh về ảnh xám để train (sử dụng bài sau)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Truy cập vào ảnh dữ liệu trên
    faces = face_cascade.detectMultiScale(gray)
    # vẽ hình vuông bao quanh khuôn mặt
    # x, y tọa độ điểm để tịnh tiến ngang dọc để lấy hình bao quanh khuôn mặt
    for(x, y, w, h) in faces:
        # vẽ hình vuông trên webcam
        # tịnh tiến trong không gian theo chiều rộng và chiều cao, lấy màu xanh (0, 255, 0) với độ dày 2
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    # show ra
    cv2.imshow('DETECTING FACE', frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
#giải phóng bộ nhớ và hủy
cap.release()
cv2.destroyAllWindows()