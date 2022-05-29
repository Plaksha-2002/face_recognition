from sys import path
from email.mime import message
from logging import root
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import mysql.connector
import cv2
import numpy as np
import os


class Train:
       def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img3=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\bg.png")
        img3=img3.resize((1530,810),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0 ,width=1530,height=810)        

        title_lbl=Label(self.root,text="Train Dataset",font=("times new roman",40,"bold"),bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=100)

        img_Top=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\Top.png")
        img_Top=img_Top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_Top)        

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=90,width=1530,height=330)
         
        #  button

        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2", font=("times new roman",30,"bold"),bg="black", fg="white" )
        b1_1.place(x=640,y=510,width=250,height=120)
# #train
#        def train_classifier(self):
#         data_dir=("data")  
#         path=[os.path.join(data_dir,file) for file in os .listdir(data_dir)]  

#         faces=[]
#         ids=[]

#         for image in path:
#             img=Image.open(image).convert('L') #gray scale
#             imageNp=np.array(img,'uint8')
#             id=int(os.path.split(image)[1].split('.')[1])

#             faces.append(imageNp)
#             ids.append(id)

#             cv2.imshow("Training",imageNp)
#             cv2.waitKey(1)==13
        
#         ids=np.array(ids)

#         #=================Train Classifier=============
#         classifier= cv2.face.LBPHFaceRecognizer_create()
#         classifier.train(faces,ids)
#         classifier.write("classifier.xml")

#         cv2.destroyAllWindows()
#         messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)
    # ==================Create Function of Traing===================
       def train_classifier(self):
         data_dir=("data")
         path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
         faces=[]
         ids=[]

         for image in path:
                 img=Image.open(image).convert('L') # conver in gray scale 
                 imageNp = np.array(img,'uint8')
                 id=int(os.path.split(image)[1].split('.')[1])

                 faces.append(imageNp)
                 ids.append(id)

                 cv2.imshow("Training",imageNp)
                 cv2.waitKey(1)==13
            
         ids=np.array(ids)
            
            #=================Train Classifier=============
         clf= cv2.face.LBPHFaceRecognizer_create()
         clf.train(faces,ids)
         clf.write("classifier.xml")

         cv2.destroyAllWindows()
         messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)








if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
