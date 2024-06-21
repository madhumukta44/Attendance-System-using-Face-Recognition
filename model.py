import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import os

def trainer(section='section_1'):
    file_path=f'sections//{section}//{section}.npz'
    path=os.path.join(os.getcwd(),file_path)
    face_embedding=np.load(path)
    Y=face_embedding['arr_1']
    EMBEDDED_X=face_embedding['arr_0']

    encoder=LabelEncoder()# class ko number ke form me represent karta hai
    encoder.fit(Y)
    Y_encoded=encoder.transform(Y)

    model=SVC(kernel='linear',probability=True)
    model.fit(EMBEDDED_X,Y_encoded)
    Y=list(set(Y))
    # students= [eval(i) for i in Y]
    Y.sort()
    students=Y.copy()
    attendence_matrix=[]
    for student in students:
        x=[]
        x.append(student)
        x.append('A')
        attendence_matrix.append(x)
    return model,encoder,attendence_matrix

if __name__=='__main__':
    face_embedding=np.load(f"C:/Users/KIIT/Minor_Project/sections/section_1/section_1.npz")
    Y=face_embedding['arr_1']
    EMBEDDED_X=face_embedding['arr_0']
    my_model,encoder,others=trainer()
    X_train,X_test,Y_train,Y_test=train_test_split(EMBEDDED_X,Y,shuffle=True,random_state=17)

    ypreds_train=my_model.predict(X_train)
    ypreds_test=my_model.predict(X_test)
    print(accuracy_score(Y,ypreds_train))
    print(accuracy_score(Y_test,ypreds_test))
