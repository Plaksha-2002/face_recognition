from logging import root
from tkinter import*
from tkinter import ttk
from webbrowser import BackgroundBrowser
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
import tkinter
from time import strftime
from datetime import datetime

class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

       #bg image
        img=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\bg.png")
        img=img.resize((1530,810),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0 ,width=1530,height=810)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",40,"bold"),bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=95)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(bg_img,font=('times new roman',14,'bold'),background='black',foreground='white')
        lbl.place(x=1400,y=732,width=130,height=50)
        time()    




         #student Button
        img4=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\student.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=260,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details ,cursor="hand2",font=("times new roman",15,"bold"),bg="black", fg="white" )
        b1_1.place(x=260,y=400,width=220,height=40)

        #detector Button
        img5=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\detector.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=645,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector" ,cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black", fg="white")
        b1_1.place(x=645,y=400,width=220,height=40)

         #Attendance Button
        img6=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\attendance.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1030,y=200,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance" ,cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black", fg="white")
        b1_1.place(x=1030,y=400,width=220,height=40)

        # # #Help Button
        # img7=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\help.jpg")
        # img7=img7.resize((220,220),Image.ANTIALIAS)
        # self.photoimg7=ImageTk.PhotoImage(img7)

        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        # b1.place(x=1100,y=200,width=220,height=220)

        # b1_1=Button(bg_img,text="Help Desk" ,cursor="hand2",font=("times new roman",15,"bold"),bg="black", fg="white" )
        # b1_1.place(x=1100,y=400,width=220,height=40)

        # #Train Button
        img8=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\train.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=260,y=480,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data" ,cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black", fg="white")
        b1_1.place(x=260,y=680,width=220,height=40)

        # #Photos Button
        img9=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\photo.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=645,y=480,width=220,height=220)

        b1_1=Button(bg_img,text="Photos" ,cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black", fg="white" )
        b1_1.place(x=645,y=680,width=220,height=40)

        # # # Developer Button
        # img10=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\developer.jpg")
        # img10=img10.resize((220,220),Image.ANTIALIAS)
        # self.photoimg10=ImageTk.PhotoImage(img10)

        # b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        # b1.place(x=800,y=480,width=220,height=220)

        # b1_1=Button(bg_img,text="Developer" ,cursor="hand2",font=("times new roman",15,"bold"),bg="black", fg="white" )
        # b1_1.place(x=800,y=680,width=220,height=40)


        # #Exit Button
        img11=Image.open(r"C:\Users\Plaksha\OneDrive\Desktop\DS\faceRecognition\college_image\exit.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1030,y=480,width=220,height=220)

        b1_1=Button(bg_img,text="Exit" ,cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="black", fg="white" )
        b1_1.place(x=1030,y=680,width=220,height=40)
 
# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project?",parent=self.root)    
        if   self.iExit>0:
             self.root.destroy()
        else:
             return 

 # ====================Function buttons===========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)    

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)             





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()