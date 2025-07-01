from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root): #call self and root window
        self.root=root
        self.root.geometry("1530x790+0+0") #to set dimensions of window
        self.root.title("Face Recognition System")

        img_bel=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\vitlogo.png")
        img_bel=img_bel.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg_bel=ImageTk.PhotoImage(img_bel) #set image

        f_lbl=Label(self.root, image=self.photoimg_bel) #set image on window create label
        f_lbl.place(x=0, y=0, width=1300, height=130) #to show image on window
        
        #face recognition label
        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1280, height=45)

        #left image
        img_left=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\faceleft.jpeg")
        img_left=img_left.resize((600, 470), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left) #set image

        f_lbl=Label(self.root, image=self.photoimg_left) #set image on window create label
        f_lbl.place(x=0, y=175, width=600, height=470) #to show image on window

        #right image
        img_right=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\faceright.webp")
        img_right=img_right.resize((700, 470), Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right) #set image

        f_lbl=Label(self.root, image=self.photoimg_right) #set image on window create label
        f_lbl.place(x=600, y=175, width=700, height=470) #to show image on window

        #button
        b1_1=Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=250, y=410, width=200, height=35)


    #=========face recognition========
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Bluecheese@11", database="face_detect")
                my_cursor = conn.cursor()
                my_cursor.execute("select name, empid, dept from employee_data where empid=" + str(id))
                record = my_cursor.fetchone()

                if record is not None:
                    name, empid, dept = record

                    if confidence > 77:  # how many images have been trained
                        cv2.putText(img, f"Name: {name}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Employee ID: {empid}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {dept}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(name, empid, dept)
                    else:  # for unknown face
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return img

        def recognize(img, clf, faceCascade):
            return draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    #========attendance========
    
    def mark_attendance(self, n, i, d):
        with open("attend.csv", "r+") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0].strip() for line in myDataList]  # Extract only the names

            entry_exists = any(entry.startswith(f"{n}, {i}, {d}") for entry in myDataList)
            if not entry_exists:  # Check if the entry does not already exist
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{n.strip()}, {i.strip()}, {d.strip()}, {dtString}, {d1}, Present")


if __name__=="__main__": #call main
    root=Tk() #call root from Toolkit
    obj=Face_Recognition(root)
    root.mainloop() #close mainloop