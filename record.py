import cv2 as cv
import pandas as pd
from mtcnn.mtcnn import MTCNN
import os
import random
from embedder import get_embedding

def scan_image(img):
    detector=MTCNN()
    mid_height,mid_width=img.shape[0]//2,img.shape[1]//2
    face_boxes=[]
    for _ in range(5): # running loop 5 time for 1 image
        mid_y,mid_x = random.randint(mid_height-300, mid_height+300),random.randint(mid_width-300, mid_width+300)
        img1 = img[0:mid_y, 0:mid_x]
        img2 = img[0:mid_y, mid_x :len(img[0])]
        img3 = img[mid_y:len(img), 0:mid_x]
        img4 = img[mid_y:len(img), mid_x:len(img[0])]
        output1 = detector.detect_faces(img1)
        output2 = detector.detect_faces(img2)
        output3 = detector.detect_faces(img3)
        output4 = detector.detect_faces(img4)
        for item in output1:
            face_boxes.append(item['box'])
        for item in output2:
            item['box'][0]+=mid_x
            face_boxes.append(item['box'])
        for item in output3:
            item['box'][1]+=mid_y
            face_boxes.append(item['box'])
        for item in output4:
            item['box'][0]+=mid_x
            item['box'][1]+=mid_y
            face_boxes.append(item['box'])
    return face_boxes

def match_faces(image_path,my_model,encoder):
    image_path='D:/Minor_Project/Cricket_dataset/Test/1.jpeg'
    img=cv.imread(image_path)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    face_boxes=scan_image(img)
    present=[]
    for box in face_boxes:
        x,y,w,h=box
        face=img[y:y+h,x:x+w]
        face=cv.resize(face,(160,160))
        test_face=get_embedding(face)
        test_face=[test_face]
        ypreds=my_model.predict(test_face)
        target=encoder.inverse_transform(ypreds)
        present.append(target[0])
    present.sort()
    return present


def mark_attendence(attendence_matrix,present):
    for student in attendence_matrix:
        if present.count(student[0]) > 3:
                student[1]='P'
    return attendence_matrix

def attendence(section,attendence_matrix):
    file_path=f'sections//{section}//{section}.csv'
    path=os.path.join(os.getcwd(),file_path)
    attendence_sheet=pd.read_csv(path)
    attendence_sheet1=pd.DataFrame(attendence_matrix,columns =['NAME', 'ATTENDENCE'])
    attendence_sheet['ATTENDENCE']=attendence_sheet1['ATTENDENCE']
    attendence_array=attendence_sheet.values.tolist()
    attendence_list=[]
    for i,student in enumerate(attendence_array):
        temp={
            "sl_no":i+1,
            "name":student[0],
            "rollno":student[1],
            "attendence":student[2]
        }
        attendence_list.append(temp)
    return attendence_list

    
    
