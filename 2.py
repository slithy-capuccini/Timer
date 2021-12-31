from tkinter import *
from tkinter import ttk
import sys
import time
global count
count =0
class stopwatch():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')   
    def start(self):
        global count
        count=0
        self.timer()   
    def stop(self):
        global count
        count=1   
    def task(self):
        self.min.append(self.d)
        print(self.min) 
        textfile=open("minutos.txt","a")
        textfile.write("\n")
        for element in self.min:
            textfile.write(element)
            textfile.write(",")

        textfile.close() 
    def enter(self):
        self.min.clear()
        self.var.set(self.entry.get())
        self.min.append(self.entry.get())
        self.min.append(self.d)
    def close(self):
        self.root.destroy()
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer)     
    def __init__(self):
        self.root=Tk()
        self.root.title("Stop Watch")
        self.root.geometry("500x200")
        self.t = StringVar()
        self.entry=ttk.Entry(self.root)
        self.var=StringVar()
        self.min=[]
        self.danger=StringVar()
        self.danger.set("DANGER ZONE")
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Times 12 bold"),bg=("green"))
        self.bt2 = Button(self.root, text="Enter", command=self.enter,font=("Times 12 bold"),bg=("blue"))
        self.bt3 = Button(self.root,text="Clock_s",command=self.stop,font=("Times 12 bold"),bg=("red"))
        self.lb2 = Label(self.root,textvariable=self.var,font=("Times 20 bold"),bg="white")
        self.lb3 = Label(self.root,textvariable=self.danger,font=("Times 20 bold"),bg="red")
        self.bt4 = Button(self.root,text="Reset",command=self.reset,font=("Times 12 bold"),bg=("orange"))
        self.bt5 = Button(self.root, text="Exit", command=self.close,font=("Times 12 bold"),bg=("yellow"))
        self.bt6 = Button(self.root,text="Stop",command=self.task,font=("Times 12 bold"),bg=("purple"))
        self.entry.place(x=20,y=10)
        self.lb.place(x=20,y=100)
        self.lb2.place(x=20,y=50)
        self.lb3.place(x=20,y=275)
        self.bt1.place(x=20,y=200)
        self.bt2.place(x=120,y=200)
        self.bt6.place(x=220,y=200)
        self.bt3.place(x=20,y=350)
        self.bt4.place(x=120,y=350)
        self.bt5.place(x=220,y=350)
        
        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.configure(bg='black')
        self.root.mainloop()
a=stopwatch()   