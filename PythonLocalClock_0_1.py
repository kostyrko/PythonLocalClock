'''simple application made for practice 
made to show local current time'''

from tkinter import *
import time

win=Tk()
win.title('Current Time')

win.geometry('250x100')
win.resizable(width=False,height=False)

def get_time():
   localtime = time.asctime( time.localtime(time.time()))
   label2=Label(win, text=localtime)
   label2.place(x=50,y=70)


label1=Label(win, text='To display time push the button below')
label1.place(x=20,y=0)

btn1=Button(win, text='Show time' , command= lambda: get_time())
btn1.place(x=90,y=30)


win.mainloop()
