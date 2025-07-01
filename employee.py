#again to create window
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Employee:
    def __init__(self, root): #call self and root window
        self.root=root
        self.root.geometry("1530x790+0+0") #to set dimensions of window
        self.root.title("Face Recognition System")

        #========variables========
        self.var_empid=StringVar() #fill these variables in comboboxes and entry fields using textvariable
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_phoneno=StringVar()
        self.var_email=StringVar()
        self.var_add=StringVar()
        self.var_dept=StringVar()
        self.var_post=StringVar()
        self.var_ro=StringVar()
        
        #header image
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
        title_lbl=Label(bg_lbl, text="EMPLOYEE MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        #create frame(buttons, labels, etc) on background image
        main_frame=Frame(bg_lbl, bd=2)
        main_frame.place(x=5, y=55, width=1257, height=450)

        #left label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employee Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=608, height=430)

        #employee information under left frame
        employee_info_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Personal Information", font=("times new roman", 12, "bold"))
        employee_info_frame.place(x=5, y=5, width=595, height=160)

        #empid label under employee info
        empid_label=Label(employee_info_frame, text="Employee ID", font=("times new roman", 12, "bold"), bg="white")
        empid_label.grid(row=0, column=0, padx=10, pady=2, sticky=W)

        #entry for employeeid
        empid_var = StringVar()  # Create a StringVar variable
        empid_entry = ttk.Entry(employee_info_frame, textvariable=self.var_empid, font=("times new roman", 12, "bold"), width=20)
        empid_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #empname label under employee info
        empname_label=Label(employee_info_frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        empname_label.grid(row=0, column=2, padx=10, pady=2, sticky=W)

        #entry for employeename
        empname_var = StringVar()  # Create a StringVar variable
        empname_entry = ttk.Entry(employee_info_frame, textvariable=self.var_name, font=("times new roman", 12, "bold"), width=20)
        empname_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #empgender label under employee info
        empgender_label=Label(employee_info_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        empgender_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        #combobox for employeegender
        gender_combo=ttk.Combobox(employee_info_frame,textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"]=("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #phoneno label under employee info
        phoneno_label=Label(employee_info_frame, text="Phone Number", font=("times new roman", 12, "bold"), bg="white")
        phoneno_label.grid(row=1, column=2, padx=10, pady=2, sticky=W)

        #entry for phoneno
        phoneno_var = StringVar()  # Create a StringVar variable
        phoneno_entry = ttk.Entry(employee_info_frame, textvariable=self.var_phoneno, font=("times new roman", 12, "bold"), width=20)
        phoneno_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #emailid label under employee info
        emailid_label=Label(employee_info_frame, text="Email ID", font=("times new roman", 12, "bold"), bg="white")
        emailid_label.grid(row=2, column=0, padx=10, pady=2, sticky=W)

        #entry for emailid
        emailid_var = StringVar()  # Create a StringVar variable
        emailid_entry = ttk.Entry(employee_info_frame, textvariable=self.var_email, font=("times new roman", 12, "bold"), width=20)
        emailid_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        #address label under employee info
        empname_label=Label(employee_info_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        empname_label.grid(row=2, column=2, padx=10, pady=2, sticky=W)

        #entry for address
        address_var = StringVar()  # Create a StringVar variable
        address_entry = ttk.Entry(employee_info_frame, textvariable=self.var_add, font=("times new roman", 12, "bold"), width=20)
        address_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        #current dept under left frame
        current_dept_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Additional Information", font=("times new roman", 12, "bold"))
        current_dept_frame.place(x=5, y=170, width=595, height=220)

        #department label under current dept
        dept_label=Label(current_dept_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dept_label.grid(row=0, column=0, padx=10, pady=2, sticky=W)

        #combobox for department
        dept_combo=ttk.Combobox(current_dept_frame,textvariable=self.var_dept, font=("times new roman", 12, "bold"), state="readonly")
        dept_combo["values"]=("Select Department", "Information Security", "HR","Sonars", "Radars", "Antennae", "Satcom (Defence)", "Electronic Manufacturing Unit")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W) #start after Department label 

        #post label under current dept
        dept_label=Label(current_dept_frame, text="Post", font=("times new roman", 12, "bold"), bg="white")
        dept_label.grid(row=0, column=2, padx=10, pady=2, sticky=W)

        #combobox for post
        post_combo=ttk.Combobox(current_dept_frame,textvariable=self.var_post, font=("times new roman", 12, "bold"), state="readonly")
        post_combo["values"]=("Select Post", "Trainee Engineer", "Senior Assistant Facility Officer","Company Secretary", "Grade Manager", "General Manager", "Security Officer", "Office Helper")
        post_combo.current(0)
        post_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W) #start after Post label

        #reporting officer label under current dept
        ro_label=Label(current_dept_frame, text="Reporting Officer", font=("times new roman", 12, "bold"), bg="white")
        ro_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        #combobox for reporting officer
        ro_combo=ttk.Combobox(current_dept_frame,textvariable=self.var_ro, font=("times new roman", 12, "bold"), state="readonly")
        ro_combo["values"]=("Select Reporting Officer", "Mr. Ajay Aggarwal", "Mr. Manoj Kumar","Ms. Nidhi", "Mrs. Sandhya Singh", "Mr. Satyendra Kumar", "Ms. Rashmi Jha", "Mr. Rajesh Kumar", "Mr. Shyam Raj")
        ro_combo.current(0)
        ro_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W) #start after RO label

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(current_dept_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=2, column=0)

        #both values can be stored in the same variable
        radiobtn2=ttk.Radiobutton(current_dept_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=2, column=1)

        #buttons frame
        btn_frame1=Frame(current_dept_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=120, width=584, height=35)

        save_btn=Button(btn_frame1, text="Save",command=self.add_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame1, text="Update",command=self.update_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame1, text="Delete",command=self.delete_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame1, text="Reset", command=self.reset_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame2=Frame(current_dept_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=0, y=160, width=584, height=35)

        take_photo_btn=Button(btn_frame2, text="Take Photo Sample", command=lambda: self.generate_dataset(self.var_empid.get()), width=31, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn=Button(btn_frame2, text="Update Photo Sample", width=31, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        
        #right label frame
        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employee Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=628, y=10, width=608, height=430)

        #search system under right frame
        Search_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=5, width=595, height=120)

        search_label=Label(Search_frame, text="Search By", font=("times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=2, sticky=W)

        search_combo=ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="readonly")
        search_combo["values"]=("Select", "Employee ID", "Employee Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W) #start after Department label

        search_var = StringVar()  # Create a StringVar variable
        search_entry = ttk.Entry(Search_frame, textvariable=search_var, font=("times new roman", 12, "bold"), width=20)
        search_entry.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        search_btn=Button(Search_frame, text="Search", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=1, column=1)

        showAll_btn=Button(Search_frame, text="Show All", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=1, column=2)

        #table frame under right frame
        table_frame=Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=130, width=595, height=259)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.emp_table=ttk.Treeview(table_frame, column=("empid", "name", "gender", "phoneno", "email", "add", "dept", "post", "ro", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        #pack scrollbars
        scroll_x.pack(side=BOTTOM, fill=X) #till bottom fill x-axis
        scroll_y.pack(side=RIGHT, fill=Y) #till right fill y-axis
        #config scrollbars with table
        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)

        self.emp_table.heading("empid", text="EmployeeID")
        self.emp_table.heading("name", text="Name")
        self.emp_table.heading("gender", text="Gender")
        self.emp_table.heading("phoneno", text="PhoneNo")
        self.emp_table.heading("email", text="EmailID")
        self.emp_table.heading("add", text="Address")
        self.emp_table.heading("dept", text="Department")
        self.emp_table.heading("post", text="Post")
        self.emp_table.heading("ro", text="ReportingOfficer")
        self.emp_table.heading("photo", text="PhotoSampleStatus")
        self.emp_table["show"]="headings"
        
        self.emp_table.column("empid", width=80)
        self.emp_table.column("name", width=100)
        self.emp_table.column("gender", width=50)
        self.emp_table.column("phoneno", width=100)
        self.emp_table.column("email", width=200)
        self.emp_table.column("add", width=80)
        self.emp_table.column("dept", width=150)
        self.emp_table.column("post", width=100)
        self.emp_table.column("ro", width=150)
        self.emp_table.column("photo", width=150)

        self.emp_table.pack(fill=BOTH, expand=1)
        self.emp_table.bind("<ButtonRelease>", self.get_cursor) #bind get_cursor with table this will enter all fields when we click on a table row
        self.fetch_data() #data will be added to table
        
    #========function to add data========
    def add_data(self):
        if self.var_empid.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phoneno.get()=="" or self.var_email.get()=="" or self.var_add.get()=="" or self.var_dept.get()=="Select Department" or self.var_post.get()=="Select Post" or self.var_ro.get()=="Select Reporting Officer":
            messagebox.showerror("Error", "All fields are required", parent=self.root) #show messagebox on same window sometimes it goes on some other window
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Bluecheese@11", database="face_detect")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into employee_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_empid.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_phoneno.get(),
                    self.var_email.get(),
                    self.var_add.get(),
                    self.var_dept.get(),
                    self.var_post.get(),
                    self.var_ro.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data() #data will be added to table
                conn.close()
                messagebox.showinfo("Success", "Employee details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    #========function to fetch entered data to table========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Bluecheese@11", database="face_detect")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee_data")
        data=my_cursor.fetchall() #this variable stores all data

        if isinstance(data, list) and len(data)!=0:
            self.emp_table.delete(*self.emp_table.get_children()) #if len(data)!=0 it means data has some value so delete its children
            #deletes all the rows in the emp_table widget before inserting new data into it. This ensures that the table only contains the most recent data
            for i in data: #insert data in table
                self.emp_table.insert("", END, values=i)
            conn.commit() #to keep on adding data
        conn.close()

    #========get cursor========
    def get_cursor(self, event=""): #bind get_cursor with table
        cursor_focus=self.emp_table.focus() #focus cursor on emp_table
        content=self.emp_table.item(cursor_focus) #take content from table
        data=content["values"] #stores values of content
        
        self.var_empid.set(data[0]), #insert values in entry field
        self.var_name.set(data[1]),
        self.var_gender.set(data[2]),
        self.var_phoneno.set(data[3]),
        self.var_email.set(data[4]),
        self.var_add.set(data[5]),
        self.var_dept.set(data[6]),
        self.var_post.set(data[7]),
        self.var_ro.set(data[8]),
        self.var_radio1.set(data[9])
        
    #update function
    def update_data(self):
        if self.var_empid.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phoneno.get()=="" or self.var_email.get()=="" or self.var_add.get()=="" or self.var_dept.get()=="Select Department" or self.var_post.get()=="Select Post" or self.var_ro.get()=="Select Reporting Officer":
            messagebox.showerror("Error", "All fields are required", parent=self.root) #show messagebox on same window sometimes it goes on some other window
        else:
            try:
                Updatee=messagebox.askyesno("Update", "Do you want to update the employee details?", parent=self.root)
                if Updatee>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Bluecheese@11", database="face_detect")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update employee_data set name=%s, gender=%s, phoneno=%s, email=%s, `add`=%s, dept=%s, post=%s, ro=%s, photosample=%s where empid=%s", (
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_phoneno.get(),
                        self.var_email.get(),
                        self.var_add.get(),
                        self.var_dept.get(),
                        self.var_post.get(),
                        self.var_ro.get(),
                        self.var_radio1.get(), 
                        self.var_empid.get()
                    ))
                else:
                    if not Updatee:
                        return
                messagebox.showinfo("Success", "Successfully updated employee details", parent=self.root)
                conn.commit() #so that data keeps on updating
                self.fetch_data() #so that whenever data is updated it gets fetched
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
            
    #delete function
    def delete_data(self):
        if self.var_empid.get()=="":
            messagebox.showerror("Error", "Employee ID is required:", parent=self.root)
        else:
            delete=messagebox.askyesno("Employee Delete Page", "Do you want to delete this employee", parent=self.root)
            if delete>0:
                conn=mysql.connector.connect(host="localhost", username="root", password="Bluecheese@11", database="face_detect")
                my_cursor=conn.cursor()
                sql="delete from employee_data where empid=%s"
                val=(self.var_empid.get(),) #value from while data is being deleted
                my_cursor.execute(sql, val)
            else:
                if not delete:
                    return
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete", "Successfully deleted employee details", parent=self.root)
            
    #reset
    def reset_data(self):
        self.var_empid.set("")
        self.var_name.set("")
        self.var_gender.set("Select Gender")
        self.var_phoneno.set("")
        self.var_email.set("")
        self.var_add.set("")
        self.var_dept.set("Select Department")
        self.var_post.set("Select Post")
        self.var_ro.set("Select Reporting Officer")
        self.var_radio1.set("")

    #generate data set or take photo samples
    #match dataset with database's data for this update don't insert because empid will show error same data won't be inserted twice
    def generate_dataset(self, emp_id):
        if self.var_empid.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phoneno.get()=="" or self.var_email.get()=="" or self.var_add.get()=="" or self.var_dept.get()=="Select Department" or self.var_post.get()=="Select Post" or self.var_ro.get()=="Select Reporting Officer":
            messagebox.showerror("Error", "All fields are required", parent=self.root) #show messagebox on same window sometimes it goes on some other window
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Bluecheese@11", database="face_detect")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee_data")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update employee_data set name=%s, gender=%s, phoneno=%s, email=%s, `add`=%s, dept=%s, post=%s, ro=%s, photosample=%s where empid=%s", (
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_phoneno.get(),
                    self.var_email.get(),
                    self.var_add.get(),
                    self.var_dept.get(),
                    self.var_post.get(),
                    self.var_ro.get(),
                    self.var_radio1.get(), 
                    self.var_empid.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #file for object detection
                def face_cropped(img):#to crop face
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #to convert to gray scale
                    faces=face_classifier.detectMultiScale(gray, 1.3, 5) #1.3 default scaling factor, 5 default min. neighbour
                    
                    #to generate rectange
                    for (x, y, w, h) in faces: #w=width, h=height
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                #to open camera
                cap = cv2.VideoCapture(0)  # Open webcam
                if not cap.isOpened():
                    messagebox.showerror("Error", "Failed to open webcam")
                else:
                    cwd = os.getcwd()
                    data_folder = os.path.join(cwd, 'data')  # Path to the "data" folder

                    # Create the "data" folder if it doesn't exist
                    if not os.path.exists(data_folder):
                        os.makedirs(data_folder)

                    img_id = 0  # Initialize image ID

                    while img_id < 100:  # Capture 100 images
                        ret, my_frame = cap.read()  # Read captured image
                        if ret and my_frame is not None:  # Check if frame is valid
                            cv2.imshow("Captured Frame", my_frame)  # Display captured frame

                            face = face_cropped(my_frame)  # Assuming face_cropped() returns cropped face
                            if face is not None:
                                face_resized = cv2.resize(face, (450, 450))
                                cv2.imshow("Cropped Face", face_resized)  # Display cropped face

                                # Save the image to the "data" folder
                                employee_id = self.var_empid.get()
                                file_name_path = os.path.join(data_folder, f'user.{emp_id}.{id}.{img_id}.jpg')
                                cv2.imwrite(file_name_path, face_resized)
                                img_id += 1  # Increment image ID

                        # Wait for a key press for a short duration (1 millisecond) to ensure responsiveness
                        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
                            break

                    # Release the webcam and close OpenCV windows
                    cap.release()
                    cv2.destroyAllWindows()

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Datasets Generated")
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)




                                  
if __name__=="__main__": #call main
    root=Tk() #call root from Toolkit
    obj=Employee(root)
    root.mainloop() #close mainloop


