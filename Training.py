import cv2
import numpy as np
import os
#thư  viện để nhập ảnh vào
from PIL import Image
# biến để training hình ảnh khuôn mặt
recognizer = cv2.face.LBPHFaceRecognizer_create()
# lấy đường dẫn do chung thư mục gốc
path = 'dataSet'
# hàm để train
def getImageWithId(path):
    # lấy ra tất cả đường dẫn của ảnh trong thư much
    imagePaths =[os.path.join(path, f) for f in os.listdir(path)]
  #  2 mảng để lưu dữ liệu ảnh và list id
    faces = []
    IDs= []
    #duyệt tất cả đường dẫn
    for imagePath in imagePaths:
        #mở ảnh lên convert về grayscale
        faceImg = Image.open(imagePath).convert('L')
        # chuyển về mảng numpy, chuyển về định dạng uint8
        faceNp = np.array(faceImg, 'uint8')
        print(faceNp)
        #ép kiểu về int, cắt để lấy ra số 1 trong tên làm id
        Id = int(imagePath.split('\\')[1].split('.')[1])
        # thêm vào mảng
        faces.append(faceNp)
        IDs.append(Id)
        cv2.imshow('training', faceNp)
        cv2.waitKey(10)
#

    return faces, IDs
# quá trình train
faces, IDs = getImageWithId(path)
recognizer.train(faces, np.array(IDs))
#lưu vào file trainningData.yml
recognizer.save('trainningData.yml')
cv2.destroyAllWindows()