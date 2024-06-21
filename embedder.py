import cv2 as cv
# import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
import os
from keras_facenet import FaceNet

class FACELOADING:
  def __init__(self,directory):
    self.directory=directory
    self.target_size=(160,160)
    self.X=[]
    self.Y=[]
    self.detector=MTCNN()

  def extract_face(self,filename):
    img=cv.imread(filename)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result=self.detector.detect_faces(img)
    x,y,w,h=result[0]['box']
    x,y=abs(x),abs(y)
    face=img[y:y+h,x:x+w]
    face_arr=cv.resize(face,self.target_size)
    return face_arr

  def load_faces(self,dir):
    FACES=[]
    for im_name in os.listdir(dir):
      try:
        path=dir+im_name
        single_face=self.extract_face(path)
        FACES.append(single_face)
      except Exception as e:
        pass
    return FACES

  def load_classes(self):
    for sub_dir in os.listdir(self.directory):
      path=self.directory+'/'+sub_dir+'/'
      FACES=self.load_faces(path)
      labels=[sub_dir for _ in range(len(FACES))]
      print(f'LOADED SUCCESSFULLY : {len(labels)}')
      self.X.extend(FACES)
      self.Y.extend(labels)
    return np.asarray(self.X), np.asarray(self.Y)

  def plot_images(self):
    for num,img in enumerate(self.X):
      ncols=3
      nrows=len(self.Y)//ncols+1
      plt.subplot(nrows,ncols,num+1)
      plt.imshow(img)
      plt.axis('off')


def get_embedding(face_img):
  embedder = FaceNet()
  face_img=face_img.astype('float32')
  face_img=np.expand_dims(face_img,axis=0)
  yhat=embedder.embeddings(face_img)
  return yhat[0]

if __name__=='__main__':
    faceloading=FACELOADING('C:/Users/KIIT/Minor_Project/Cricket_dataset/Train')
    X,Y=faceloading.load_classes()
    EMBEDDED_X=[]
    for img in X:
        EMBEDDED_X.append(get_embedding(img))
    EMBEDDED_X=np.asarray(EMBEDDED_X)
    np.savez_compressed('C:/Users/KIIT/Minor_Project/sections/section_1/section_1.npz',EMBEDDED_X,Y)
