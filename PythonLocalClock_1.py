'''simple application made for practice 
made to show local current time'''

from tkinter import *
import time
import datetime

win=Tk()
win.title('Current Time ver. 1.1')

win.geometry('250x150')
win.resizable(width=False,height=False)

def get_time():
   localtime = time.strftime('%H:%M:%S',time.localtime())
   label2=Label(win, text=localtime)
   result.insert(END,'{0:^30}\n'.format(localtime))
   # label2.place(x=95,y=90)

def get_date():
   date_today=datetime.date.today().isoformat()
   label2=Label(win, text=date_today)
   result.insert(END, '{0:^30}\n'.format(date_today))
   #label2.place(x=88,y=115)

def clear():
    result.delete("1.0", END)


label1=Label(win, text='Display time or date by pushing a button')
label1.place(x=14,y=5)

btn1=Button(win, text='Show time' , command= lambda: get_time())
btn1.place(x=10,y=30)
btn2=Button(win, text='Show date', command= lambda:get_date())
btn2.place(x=100,y=30)
btn3=Button(win, text='Clear', command= lambda:clear())
btn3.place(x=190,y=30)

result = Text(win)
result.place(x=0,y=90)

win.mainloop()
