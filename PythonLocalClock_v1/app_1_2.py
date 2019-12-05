''' simple application using tkinter and datetime model
made for practice -> displays local current time and date '''

import tkinter as tk
import time
import datetime

class PythonLocalClock:
    def __init__(self,master):
        self.master = master
        master.title('Current Time ver. 1.2.1')

        self.label = tk.Label(master, 
                            text='Push a button to see current time or date',
                            relief="sunken")
        self.label.pack()

        self.time_button = tk.Button(master,width=8, 
                                    text='Show time', bg="yellow green",
                                    command =self.get_time)
        self.time_button.pack()

        self.date_button = tk.Button(master,width=8, 
                                    text='Show date', bg= "SteelBlue3",
                                    command =self.get_date)
        self.date_button.pack()

        self.clear = tk.Button(master,width=8, text='Clear', bg="red3",
                                command =self.clear)
        self.clear.pack()

        self.result = tk.Text(master, height=5, width=20)
        self.result.pack()

    def get_time(self):
        local_time = time.strftime('%H:%M:%S',time.localtime())
        self.result.insert(tk.END,'{0:^20}\n'.format(local_time))

    def get_date(self):
        date_today=datetime.date.today().isoformat()
        self.result.insert(tk.END, '{0:^20}\n'.format(date_today))

    def clear(self):
        self.result.delete("1.0", tk.END)


def main():
    root = tk.Tk()
    app = PythonLocalClock(root)
    root.mainloop()

if __name__ == '__main__':
    main()