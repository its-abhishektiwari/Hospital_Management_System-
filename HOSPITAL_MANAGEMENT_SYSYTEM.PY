from tkinter import*
from tkinter import ttk
import random
import time 
import datetime
from tkinter import messagebox

import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0") 

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot-StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",FG="RED",BG="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #==================================dataframe======================================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.pack(x=0,y=130,width=1530,height=400)

        DataframeLeft=Label(Dataframe,bd=10,relief=RIDGE,padx=10,
                            
                                 font=("arial",12,"bold"),text="patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        DataframeRight=Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.pack(x=0,y=130,width=1530,height=400)

        DataframeRight=Label(Dataframe,bd=10,relief=RIDGE,padx=10,
                            
                                 font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=360)
        #===========================button frame=======================================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.pack(x=0,y=130,width=530,height=70)
        #===========================details frame=======================================================
        detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        detailsframe.pack(x=0,y=600,width=1530,height=190)

        #====================================DataframeLeft=========================================================
        lblNameTablet=Label(DataframeLeft,text="Name of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(Dataframe,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=33)
        comNametablet['values']=("phenoxymethylpenicillin", "ampicillin", "amoxicillin","flucloxacillin","paracetamol")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial", 12, "bold"), text="Refence No:", padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial", 13, "bold"), extvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft, font=("arial", 13, "bold"),extvariable=self.dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft, font=("arial", 12, "bold"), text="No Of Tablets::", padx=2, pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft, font=("arial", 13, "bold"), extvariable=self.Nameoftablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4,column=0, sticky=W)
        txtLot=Entry(DataframeLeft, font=("arial", 13, "bold"),extvariable=self.lot, width=35)
        txtLot.grid(row=4,column=1) 

        lblissueDate=Label (DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft, font=("arial", 13, "bold"),extvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label (DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry (DataframeLeft, font=("arial", 13, "bold"), extvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft, font=("arial", 13, "bold"), extvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label (DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry (DataframeLeft, font=("arial", 13, "bold"), extvariable=self.sideEfect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label (DataframeLeft, font=("arial", 12, "bold"), text="Further Information", padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft, font=("arial", 12, "bold"),extvariable=self.FurtherInformation, width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure", padx=2, pady=6)
        lblBloodPressure.grid(row=1,column=2,stickv=W)
        txtBloodPressure=Entry(DataframeLeft, font=("arial", 12, "bold"),extvariable=self.DrivingUsingMachine, width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft , font=("arial", 12, "bold"), text="Storage Advice:",padx=2, pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft, font=("arial", 12, "bold"),extvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication", padx=2, pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft, font=("arial", 12, "bold"), extvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)

        lblPatientId=Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4,column=2, sticky=W)
        txtPatientId=Entry(DataframeLeft, font=("arial", 12, "bold"),extvariable=self.PatientIda,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2, pady=6)
        lblNhsNumber.grid(row=5,column=2, sticky=W)
        txtNhsNumber=Entry(DataframeLeft, font=("arial", 12, "bold"), extvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft, font=("arial", 12, "bold"), extvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft, font=("arial", 12, "bold"), text="Date Of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft, font=("arial", 12, "bold"),extvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft, font=("arial", 12, "bold"),extvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8,column=3)


        #==========================================data frame right=======================================================================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #======================================BUTTON===========================================
        btnpresciption=Button(Buttonframe,text="Presciption",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnpresciption.grid(row=0,column=0)

        btnpresciptionData=Button(Buttonframe,text="Presciption Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnpresciptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #===========================================Table=============================================================================
        #===========================================Scrollbar==============================================================================
        Scrollbar_x=ttk.Scrollbar(detailsframe,HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(detailsframe,column=("nameoftable","ref","Nooftablets","lot","issuedate","dose",
                                                              "expdate","dailydose","storage","nhsnumber","pname","dob","address")xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
            

        Scroll_x.pack=(side=BOTTOM,fill=x)
        Scroll_y.pack=(side=RIGHT,fill=Y)

        
        Scrollbar_x=ttk.Scrollbar(command=self.hospital_table.xview)
        Scrollbar_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"
    
        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100) 

        self.hospital_table.pack(fill=BOTH,expand=1)



        #=========================function declration================================
        
        def iPrescriptionData(self):
            if self.Nameoftablets.get()=="" or self.ref.get()="":
             messagebox.showerror("Error","All fields are required")
            else:
               conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
               my_cursor=conn.cursor()












root=Tk()
ob=Hospital(root)
root.mainloop()

