from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root): #call self and root window
        self.root=root
        self.root.geometry("1530x790+0+0") #to set dimensions of window
        self.root.title("Face Recognition System")

        img_bel=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\vitlogo.png")
        img_bel=img_bel.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg_bel=ImageTk.PhotoImage(img_bel) #set image

        f_lbl=Label(self.root, image=self.photoimg_bel) #set image on window create label
        f_lbl.place(x=0, y=0, width=1300, height=130) #to show image on window
        
        #train dataset label
        title_lbl=Label(self.root, text="TRAIN DATASET", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1280, height=45)
    
        #top image
        img_top=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\traindataimg1.png")
        img_top=img_top.resize((1300, 200), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top) #set image

        f_lbl=Label(self.root, image=self.photoimg_top) #set image on window create label
        f_lbl.place(x=0, y=175, width=1300, height=200) #to show image on window

        #button
        b1_1=Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=0, y=382, width=1300, height=50)

        #bottom image
        img_bottom=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\traindataimg2.png")
        img_bottom=img_bottom.resize((1300, 200), Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom) #set image

        f_lbl=Label(self.root, image=self.photoimg_bottom) #set image on window create label
        f_lbl.place(x=0, y=440, width=1300, height=200) #to show image on window

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[] #images of the same person must have the same id
        for image in path:
            img=Image.open(image).convert('L') #to covert image to grayscale
            imageNp=np.array(img, 'uint8') #to convert image to grid we use numpy it gives better performance for array conversion, unit8 is a data type
            id=int(os.path.split(image)[1].split('.')[1])
            #"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\data\user.1.40.jpg"
            #[0                                                            ][1           ]
            #                                                               [0,  1, 2]

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #========train the classifier and save========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids) #train data
        clf.write("classifier.xml") #trained data will be written here
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")

        
if __name__=="__main__": #call main
    root=Tk() #call root from Toolkit
    obj=Train(root)
    root.mainloop() #close mainloop