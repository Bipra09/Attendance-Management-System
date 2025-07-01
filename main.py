from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from employee import Employee
import os #to take photos directly from directory ie os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recog_Sys:
    def __init__(self, root): #call self and root window
        self.root=root
        self.root.geometry("1530x790+0+0") #to set dimensions of window
        self.root.title("Face Recognition System")
        
        #header
        img=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\vitlogo.png")
        img=img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) #set image

        f_lbl=Label(self.root, image=self.photoimg) #set image on window create label
        f_lbl.place(x=0, y=0, width=1300, height=130) #to show image on window

        #bg image
        bg_img=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\download (1).jpeg")
        bg_img=bg_img.resize((1280, 520), Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img) #set image

        bg_lbl=Label(self.root, image=self.bg_photoimg) #set image on window create label
        bg_lbl.place(x=0, y=130, width=1280, height=520) #to show image on window

        #label above bg image
        title_lbl=Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        #employee button
        img2=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\employee.jpeg")
        img2=img2.resize((220, 150), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2) #set image

        b1=Button(bg_lbl, image=self.photoimg2,command=self.employee_details, cursor="hand2") #set image on window create label and link student details page to home page
        b1.place(x=100, y=100, width=220, height=150) #to show image on window

        #employee button name tag
        b1_1=Button(bg_lbl, text="Employee Details",command=self.employee_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=250, width=220, height=25)
        
        #detect face button
        img3=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\facedetect.jpeg")
        img3=img3.resize((220, 150), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) #set image

        b1=Button(bg_lbl, image=self.photoimg3, cursor="hand2", command=self.face_data) #set image on window create label
        b1.place(x=500, y=100, width=220, height=150) #to show image on window

        #detect face name tag
        b1_1=Button(bg_lbl, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=250, width=220, height=25)

        #attendance face button
        img4=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\attendance.png")
        img4=img4.resize((220, 150), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4) #set image

        b1=Button(bg_lbl, image=self.photoimg4, cursor="hand2", command=self.attendance_data) #set image on window create label
        b1.place(x=900, y=100, width=220, height=150) #to show image on window

        #attendance name tag
        b1_1=Button(bg_lbl, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=900, y=250, width=220, height=25)

        
        #train face button
        img6=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\train.jpeg")
        img6=img6.resize((220, 150), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6) #set image

        b1=Button(bg_lbl, image=self.photoimg6, cursor="hand2", command=self.train_data) #set image on window create label
        b1.place(x=100, y=300, width=220, height=150) #to show image on window

        #train face name tag
        b1_1=Button(bg_lbl, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=450, width=220, height=25)

        #photos button
        img7=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\photos.jpeg")
        img7=img7.resize((220, 150), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7) #set image

        b1=Button(bg_lbl, image=self.photoimg7, cursor="hand2", command=self.open_image) #set image on window create label
        b1.place(x=500, y=300, width=220, height=150) #to show image on window

        #photos name tag
        b1_1=Button(bg_lbl, text="Photos", cursor="hand2", command=self.open_image, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=450, width=220, height=25)

        
    def open_image(self):
        os.startfile("data")


    #=======function buttons========
    def employee_details(self):
        self.new_window=Toplevel(self.root) #create new window on top of main home page
        self.app=Employee(self.new_window) #new variable to declare class Employee

    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Attendance(self.new_window)
    

if __name__=="__main__": #call main
    root=Tk() #call root from Toolkit
    obj=Face_Recog_Sys(root)
    root.mainloop() #close mainloop
