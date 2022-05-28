from tkinter import*
from tkinter import ttk
from turtle import bgcolor, width
from unittest import result
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("15600x800+0+0")
        self.root.title("Attendance System")

        # variables
        self.attenID = StringVar()
        self.attenRoll = StringVar()
        self.attenName = StringVar()
        self.attenDept = StringVar()
        self.attenTime = StringVar()
        self.attenDate = StringVar()
        self.attenAttendance = StringVar()


        #image1
        img4=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student.jpg")
        img4=img4.resize((800,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl = Label(self.root,image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #image2
        img5=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student2.jpg")
        img5=img5.resize((800,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        f_lbl = Label(self.root,image=self.photoimg5)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #bg image
        img3=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\attendance.jpg")
        img3=img3.resize((1530,800),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b_lbl = Label(self.root,image=self.photoimg3)
        b_lbl.place(x=0,y=200,width=1530,height=800)

        title_lbl= Label(b_lbl,text="STUDENT ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #will make frame
        main_frame=Frame(b_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=520)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student attendance details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=480)

        img2=Image.open(r"C:\Users\ANNANYA\OneDrive\Desktop\face_recog\images\student1.jpg")
        img2=img2.resize((770,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl = Label(left_frame,image=self.photoimg2)
        f_lbl.place(x=5,y=0,width=770,height=100)

        left_inside_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=0,y=105,width=720,height=350)

        ##labels

        #attendance
        attendanceID_lbl=Label(left_inside_frame,text="Attendance Id",font=("times new roman",12,"bold"),bg="white")
        attendanceID_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        attendanceIDEntry=ttk.Entry(left_inside_frame,textvariable=self.attenID,width=20,font=("times new roman",15,"bold"))
        attendanceIDEntry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_lbl=Label(left_inside_frame,text="Roll no",font=("times new roman",12,"bold"),bg="white")
        roll_lbl.grid(row=0,column=2,padx=4,pady=8,sticky=W)
        rollEntry=ttk.Entry(left_inside_frame,width=20,textvariable=self.attenRoll,font=("times new roman",15,"bold"))
        rollEntry.grid(row=0,column=3,pady=8,sticky=W)

        #name
        name_lbl=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        name_lbl.grid(row=1,column=0)
        nameEntry=ttk.Entry(left_inside_frame,width=20,textvariable=self.attenName,font=("times new roman",15,"bold"))
        nameEntry.grid(row=1,column=1,pady=8)

        #deptartment
        dept_lbl=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_lbl.grid(row=1,column=2)
        deptEntry=ttk.Entry(left_inside_frame,width=20,textvariable=self.attenDept,font=("times new roman",15,"bold"))
        deptEntry.grid(row=1,column=3,pady=8)

        #time
        time_lbl=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_lbl.grid(row=2,column=0)
        timeEntry=ttk.Entry(left_inside_frame,width=20,textvariable=self.attenTime,font=("times new roman",15,"bold"))
        timeEntry.grid(row=2,column=1,pady=8)

        #date
        date_lbl=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_lbl.grid(row=2,column=2)
        dateEntry=ttk.Entry(left_inside_frame,width=20,textvariable=self.attenDate,font=("times new roman",15,"bold"))
        dateEntry.grid(row=2,column=3,pady=8)

        #attendance
        attn_lbl=Label(left_inside_frame,text="Attendance",font=("times new roman",12,"bold"),bg="white")
        attn_lbl.grid(row=3,column=0)

        attn_combo=ttk.Combobox(left_inside_frame,textvariable=self.attenAttendance,font=("times new roman",12,"bold"),state="readonly",width=20)
        attn_combo["values"]=("Status","Present","Absent")
        attn_combo.current(0)
        attn_combo.grid(row=3,column=1,padx=10,pady=8,sticky=W)

         #buttons frame
        bt_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        bt_frame.place(x=5,y=300,width=700,height=60)

        #button to import csv data
        import_bt=Button(bt_frame,text="Import csv",command=self.importcsv,width=22,font=("times new roman",13,"bold"),bg="red",fg="white")
        import_bt.grid(row=0,column=0)

         #button to export csv data
        export_bt=Button(bt_frame,text="Export csv",command=self.exportcsv,width=22,font=("times new roman",13,"bold"),bg="red",fg="white")
        export_bt.grid(row=0,column=1)

         #button to reset data
        re_bt=Button(bt_frame,text="Reset",width=23,command=self.reset,font=("times new roman",13,"bold"),bg="red",fg="white")
        re_bt.grid(row=0,column=2)

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=480)

        #buttons frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=445)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(table_frame,column=("id","roll","name","dept","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id",text="ID")
        self.attendance_table.heading("roll",text="Roll No")
        self.attendance_table.heading("name",text="Name")
        self.attendance_table.heading("dept",text="Department")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("attendance",text="Attendance")
        self.attendance_table["show"]="headings"


        self.attendance_table.column("id",width=100)
        self.attendance_table.column("roll",width=100)
        self.attendance_table.column("name",width=100)
        self.attendance_table.column("dept",width=100)
        self.attendance_table.column("time",width=100)
        self.attendance_table.column("date",width=100)
        self.attendance_table.column("attendance",width=100)

        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.getcursor)
        #self.fetch()
        
    ## to fatch all the data
    def fetch(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    ## data to import from csv file
    def importcsv(self):
        global mydata
        mydata.clear()
        fn=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fn) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch(mydata)

    ## export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found",parent=self.root)
                return False
            fn=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fn,mode="w",newline="") as myfile:
                csvwrite=csv.writer(myfile,delimiter=",")
                for i in csvwrite:
                    csvwrite.writerow(i)
                messagebox.showinfo("Sucess","Successfully data exported",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Reason for exception:{str(e)}",parent=self.root)

    ## for cursor
    def getcursor(self,event=""):
        focus_courser=self.attendance_table.focus()
        content=self.attendance_table.item(focus_courser)
        result=content["values"]

        self.attenID.set(result[0]),
        self.attenRoll.set(result[1]),
        self.attenName.set(result[2]),
        self.attenDept.set(result[3]),
        self.attenTime.set(result[4]),
        self.attenDate.set(result[5]),
        self.attenAttendance.set(result[6]),

    ##def reset
    def reset(self):
        self.attenID.set("")
        self.attenRoll.set("")
        self.attenName.set("")
        self.attenDept.set("")
        self.attenTime.set("")
        self.attenDate.set("")
        self.attenAttendance.set("Status")



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()