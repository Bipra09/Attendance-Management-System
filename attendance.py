from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root): #call self and root window
        self.root=root
        self.root.geometry("1530x790+0+0") #to set dimensions of window
        self.root.title("Face Recognition System")

        img_bel=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\vitlogo.png")
        img_bel=img_bel.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg_bel=ImageTk.PhotoImage(img_bel) #set image

        f_lbl=Label(self.root, image=self.photoimg_bel) #set image on window create label
        f_lbl.place(x=0, y=0, width=1300, height=130) #to show image on window
        
        #attendance label
        title_lbl=Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1280, height=45)

        #bg image
        bg_img=Image.open(r"C:\Users\sanjay\OneDrive\Desktop\FACE_RECOGNITION_SYSTEM\images\bg2.jpg")
        bg_img=bg_img.resize((1280, 520), Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img) #set image

        bg_lbl=Label(self.root, image=self.bg_photoimg) #set image on window create label
        bg_lbl.place(x=0, y=175, width=1280, height=465) #to show image on window

        main_frame=Frame(bg_lbl, bd=2)
        main_frame.place(x=5, y=15, width=1257, height=430)

        #left label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=608, height=400)

        left_inside_frame=Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=10, width=590, height=300)       

        #labels and entries

        attendanceid_label=Label(left_inside_frame, text="Attendance ID", font=("times new roman", 12, "bold"), bg="white")
        attendanceid_label.grid(row=0, column=0, padx=10, pady=2, sticky=W)
        attendanceid_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), width=15)
        attendanceid_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        name_label=Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=2, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), width=15)
        name_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        dept_label=Label(left_inside_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dept_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)
        dept_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), width=15)
        dept_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        date_label=Label(left_inside_frame, text="Date", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=1, column=2, padx=10, pady=2, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), width=15)
        date_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        time_label=Label(left_inside_frame, text="Time", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=2, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, font=("times new roman", 12, "bold"), width=15)
        time_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        attendance_label=Label(left_inside_frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=2, column=2, padx=10, pady=2, sticky=W)
        attendance_combo=ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly", width=13)
        attendance_combo["values"]=("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        #buttons frame
        btn_frame1=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=250, width=584, height=35)

        save_btn=Button(btn_frame1, text="Import csv", command=self.importCsv, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame1, text="Export csv", command=self.exportCsv, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame1, text="Update", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame1, text="Reset", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        #right label frame
        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employee Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=628, y=10, width=608, height=400)

        table_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 12, "bold"))
        table_frame.place(x=5, y=5, width=595, height=200)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame, column=("id", "name", "dept", "date", "time", "stat"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        #pack scrollbars
        scroll_x.pack(side=BOTTOM, fill=X) #till bottom fill x-axis
        scroll_y.pack(side=RIGHT, fill=Y) #till right fill y-axis
        #config scrollbars with table
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="AttendanceID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("dept", text="Department")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("stat", text="Attendance Status")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("dept", width=150)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("stat", width=150)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)


    #========fetch data========
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")), parent=self.root)
        if fln:
            with open(fln, newline='') as myfile:
                csvread = csv.reader(myfile)
                mydata = list(csvread)
                self.fetchData(mydata)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for row in rows:
            self.AttendanceReportTable.insert("", END, values=row)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

if __name__=="__main__": #call main
    root=Tk() #call root from Toolkit
    obj=Attendance(root)
    root.mainloop() #close mainloop