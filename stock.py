import os
from re import I
from tkinter import ttk
from tkinter import *
from turtle import width

root=Tk()
root.title("Window")
root.geometry("1520x720+0+0")
root.resizable(0,0)
root.configure(background="white")

selected_groups_frame=Frame(root,bg="white",relief=RAISED,bd=2)
selected_groups_frame.place(x=10,y=35,width=1300,height=650)
l11=Label(root,text="c-name",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
l11.grid(row=0,column=1,ipadx=500,sticky=W)
l1=Label(root,text="Select stock group analysis",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
l1.grid(row=0,column=0,ipadx=10,)
f0=Frame(root,height=650,width=180,bg="white",relief=RAISED,bd=5)
f0.place(x=1322,y=35,width=195,height=650)

f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=4)
f11.grid(row=1,column=0,columnspan=3,ipadx=200)
l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=5,relief=GROOVE,width=20,height=6)
l1f1.pack(fill=X,pady=2,padx=2)
f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
f12.place(x=610,y=0,width=680,height=80)
l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
l1f2.place(x=305,y=10,anchor="center")
l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
l1f3.place(x=305,y=30,anchor="center")
l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
l1f4.place(x=305,y=50,anchor="center")

f13=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
f13.place(x=0,y=145,width=607,height=450)


f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
f14.place(x=610,y=83,width=340,height=58)
l1f5=Label(f14,text="INWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
l1f5.place(x=0,y=0,anchor="nw")
l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
l1f6.place(x=0,y=30,anchor="nw")
l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
l1f7.place(x=80,y=30,anchor="nw")
l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
l1f8.place(x=180,y=30,anchor="nw")



f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
f15.place(x=950,y=83,width=340,height=58)
l2f5=Label(f15,text="OUTWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
l2f5.place(x=0,y=0,anchor="nw")
l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
l2f6.place(x=0,y=30,anchor="nw")
l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
l2f7.place(x=80,y=30,anchor="nw")
l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
l2f8.place(x=180,y=30,anchor="nw")

f16=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
f16.place(x=610,y=145,width=340,height=450)
l3f6=Label(f16,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l3f6.place(x=0,y=0,anchor="nw")
l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l3f7.place(x=80,y=0,anchor="nw")
l3f8=Label(f16,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l3f8.place(x=180,y=0,anchor="nw")
        

f17=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
f17.place(x=950,y=145,width=340,height=450)
l4f6=Label(f17,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l4f6.place(x=0,y=0,anchor="nw")
l4f7=Label(f17,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l4f7.place(x=80,y=0,anchor="nw")
l4f8=Label(f17,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l4f8.place(x=180,y=0,anchor="nw")


       
f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
f18.place(x=0,y=598,width=607,height=48)
l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l5f6.place(x=0,y=0,anchor="nw")

f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
f19.place(x=610,y=598,width=340,height=48)
l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l6f6.place(x=0,y=0,anchor="nw")

f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
f20.place(x=950,y=598,width=340,height=48)
l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
l7f6.place(x=0,y=0,anchor="nw")




        























root.mainloop()
