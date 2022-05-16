from tkinter import *
import tkinter as tk
from tkinter import messagebox
# from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk


def account():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.10, relheight=0.800, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.15, rely=0.105, relheight=0.8, relwidth=0.700)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

    




global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#848884")
screen.configure(cursor="arrow")
          
sbmibtn=Button(screen,text='K:Company',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=account).place(x=20,y=10)

sbmibtn=Button(screen,text='Print',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1130,y=10)
sbmibtn=Button(screen,text='Date',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1270,y=10)
sbmibtn=Button(screen,text='Company',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1400,y=10)

global Canvas1
Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.800, relwidth=.850,)
Label5 = Label(Canvas1,text='Profit & loss ac',borderwidth="0", width=5, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",)
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999,)


global Canvas2
Canvas2 = tk.Canvas(Canvas1, background="#ffffff", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas2.place(relx=0, rely=0.0300, relheight=0.07, relwidth=0.499)
Label6 = Label(Canvas2,text='Particulars',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 12  ")
Label6.place(relx=0, rely=0.20, relheight=0.30, relwidth=0.300)

Label8 = Label(Canvas2,text='ABC Pvt Ltd',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 12  ")
Label8.place(relx=0.75, rely=0.10, relheight=0.30, relwidth=0.300)

Label10 = Label(Canvas2,text='For 1-Apr-22',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 10  ")
Label10.place(relx=0.75, rely=0.6, relheight=0.30, relwidth=0.300)

global Canvas5
Canvas5 = tk.Canvas(Canvas1, background="#ffffff", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas5.place(relx=0.500, rely=0.0300, relheight=0.07, relwidth=0.499)
Label7 = Label(Canvas5,text='Particulars',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 12  ")
Label7.place(relx=0, rely=0.20, relheight=0.30, relwidth=0.300)

Label8 = Label(Canvas5,text='ABC Pvt Ltd',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 12  ")
Label8.place(relx=0.75, rely=0.10, relheight=0.30, relwidth=0.300)

Label10 = Label(Canvas5,text='For 1-Apr-22',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 10  ")
Label10.place(relx=0.75, rely=0.6, relheight=0.30, relwidth=0.300)

global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)

global Canvas6
Canvas6 = tk.Canvas(Canvas1, background="#ffffff", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas6.place(relx=0.500, rely=0.100, relheight=0.9, relwidth=0.499)

Label6 = Label(Canvas6,text='Opening Stock',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 12  ")
Label6.place(relx=0, rely=0.1, relheight=0.30, relwidth=0.300)

Label8 = Label(Canvas6,text='ABC Pvt Ltd',borderwidth="0", width=11, background="white",
                                     foreground="#000000",
                                     font="-family {Segoe UI} -size 12  ")
Label8.place(relx=0.75, rely=0.10, relheight=0.30, relwidth=0.300)

global Canvas7
Canvas7 = tk.Canvas(Canvas1, background="#ffffff", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas7.place(relx=0, rely=0.100, relheight=200, relwidth=0.499)


screen.mainloop()