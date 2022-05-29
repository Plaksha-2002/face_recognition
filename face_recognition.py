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
from time import strftime
from datetime import datetime
from re import L


class Face_recognition:
       def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",40,"bold"),bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=100)  

        # img_Top=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\Top.png")
        # img_Top=img_Top.resize((750,700),Image.ANTIALIAS)
        # self.photoimg_Top=ImageTk.PhotoImage(img_Top)        

        # # set image as lable
        # f_lb1 = Label(self.root,image=self.photoimg_Top)
        # f_lb1.place(x=0,y=90,width=750,height=700)  


        # img_bottom=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\Top.png")
        # img_bottom=img_bottom.resize((750,700),Image.ANTIALIAS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)        

        # # set image as lable
        # f_lb1 = Label(self.root,image=self.photoimg_bottom)
        # f_lb1.place(x=750,y=90,width=750,height=700)    
        img3=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\recognition.png")
        img3=img3.resize((1530,810),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100 ,width=1530,height=710)                         

#button
        b1=Button(bg_img,text="Face Recognition", cursor="hand2",command=self.face_recog, font=("times new roman",18,"bold"),bg="red",fg="white")
        b1.place(x=650,y=250,width=250,height=80)
    #=====================Attendance===================

       def mark_attendance(self,i,r,n):
            with open("attendance.csv","r+",newline="\n") as f:
                myDatalist=f.readlines()
                name_list=[]
                for line in myDatalist:
                    entry=line.split((","))
                    name_list.append(entry[0])

                if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")

    #================face recognition==================
       def face_recog(self):
            def draw_boundray(img,classifier,scaleFactor,minNeighbour,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

                coord=[]
                
                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                    confidence=int((100*(1-predict/300)))

                    conn = mysql.connector.connect(username='root', password='Plaksha@2002',host='localhost',database='face_recognizer',port=3306)
                    cursor = conn.cursor()

                    cursor.execute("select Name from student where Student_id="+str(id))
                    n=cursor.fetchone()
                    n="+".join(n)

                    cursor.execute("select Roll from student where Student_id="+str(id))
                    r=cursor.fetchone()
                    r="+".join(r)

                    cursor.execute("select Student_id from student where Student_id="+str(id))
                    i=cursor.fetchone()
                    i="+".join(i)


                    if confidence > 77:
                        cv2.putText(img,f"Student_id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                        cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                        cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                        self.mark_attendance(i,r,n)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                    coord=[x,y,w,y]
                
                return coord    


            #==========
            def recognize(img,clf,faceCascade):
                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
            
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            videoCap=cv2.VideoCapture(0)

            while True:
                ret,img=videoCap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Face Detector",img)

                if cv2.waitKey(1) == 13:
                    break
            videoCap.release()
            cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()