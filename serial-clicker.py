import pyautogui
from time import time,sleep
from win32api import GetSystemMetrics
from tkinter import Radiobutton,Button,Label,Frame,TOP,Tk,LEFT,X,StringVar,LabelFrame
from tkinter.ttk import Entry
from random import randrange

"""
variables purpose
clicktype--> defines type of mouse click viz single,double
you can also add other - triple, middle, right etc
interval--> time interval in seconds for which mouse is repeatedly clicked
healingtime--> time interval during which no clicks are performed
This can earn the user some time to either kill this process or to give user the impression that the process has stopped completely

P.S: If you want a chance to be evil, this is the time ;-) just set 
clicktype-->triple,
interval-->anything very large,
healingtime-->0
"""


#execute the auto clicker code
def startCode(clicktype="single",interval=0.5,healingtime=0.5):
    
    start=time()
    root.destroy()
    while True:
        if clicktype=="single":
            pyautogui.click(randrange(0,GetSystemMetrics(0)),randrange(0,GetSystemMetrics(1)))
        elif clicktype=="double":
            pyautogui.doubleClick(randrange(0,GetSystemMetrics(0)),randrange(0,GetSystemMetrics(1)))
        elif clicktype=="triple":
            pyautogui.tripleClick(randrange(0,GetSystemMetrics(0)),randrange(0,GetSystemMetrics(1)))
        
        end=time()
        if(end-start>interval):
            sleep(healingtime)
            start=time()
            end=time()
            


def startUI():
    global root
    root=Tk()
    root.title("Serial Clicker")
    # root.geometry("400x400")
    # root.resizable(0,0)
    root.configure(bg="#333333")

    Label(root,text="Serial Clicker",font=('Helvetica',20,'bold'),bg="#333333",fg="white").pack(pady=5)
    frame=LabelFrame(root,bg="#1E1E1E",fg="white")
    frame.pack(side=TOP,padx=25,pady=10,ipadx=10,ipady=10)

    frame1=Frame(frame,bg="#1E1E1E")
    frame2=Frame(frame,bg="#1E1E1E")
    frame3=Frame(frame,bg="#1E1E1E")
    frame1.pack(side=TOP,pady=7)
    frame2.pack(side=TOP,pady=7)
    frame3.pack(side=TOP,pady=7)

    v=StringVar()
    v.set("single")

    interval=Entry(frame1)
    healingtime=Entry(frame2)
    interval.focus_force()
    healingtime.focus_force()
    intervall=Label(frame1,text="Interval(in s) ",bg="#1E1E1E",fg="white")
    healingl=Label(frame2,text="Healing time",bg="#1E1E1E",fg="white")
    intervall.pack(side=LEFT,padx=3,pady=5,fill=X)
    interval.pack(side=LEFT,fill=X)
    healingl.pack(side=LEFT,padx=3,pady=5)
    healingtime.pack(side=LEFT)



    Radiobutton(frame3,text="Single",variable=v,value="single",bg="#1E1E1E",fg="white").pack(side=LEFT)
    Radiobutton(frame3,text="Double",variable=v,value="double",bg="#1E1E1E",fg="white").pack(side=LEFT)
    Radiobutton(frame3,text="Triple",variable=v,value="triple",bg="#1E1E1E",fg="white").pack(side=LEFT)

    try:
        button=Button(root,text="Start",bg="#1E1E1E",fg="white",width=10,command=lambda : startCode(v.get(),int(interval.get()),int(healingtime.get())))
        button.pack(side=BOTTOM,pady=10,ipadx=10,ipady=2)
    except:
        print("enter")
    root.mainloop()

if __name__ == "__main__":
    startUI()