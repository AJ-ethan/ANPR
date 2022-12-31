'''from tkinter import *
import time
from threading import *
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("400x400")
  
# use threading
  
def threading():
    # Call work function
    t1=Thread(target=work)
    t1.start()
  
# work function
def work():
  
    print("sleep time start")
  
    for i in range(10):
        print(i)
        time.sleep(1)
  
    print("sleep time stop")
  
# Create Button
Button(root,text="Click Me",command = threading).pack()
  
# Execute Tkinter
root.mainloop()

'''

import threading
from tkinter import *
import time
from random import randint
# Initialize a new window
root=Tk()
root.geometry('500x400')
# A function that interrupts for five seconds
def five_seconds():
    time.sleep(5)

    label.config(text='5 seconds up!')
# A function that generates a random number
def random_numbers():
    rand_label.config(text=f'The random number is: {randint(1,100)}')

label=Label(root,text='Hello there!')
label.pack(pady=20)
# A button that calls a function
button1=Button(root,text='5 seconds',command=threading.Thread(target=five_seconds).start())
button1.pack(pady=20)

button2=Button(root,text='pick a random number',command=random_numbers)
button2.pack(pady=20)
rand_label=Label(root,text='')
rand_label.pack(pady=20)
root.mainloop()
'''
from threading import *
from tkinter import *
from time import *
# Declare an instance of TK class
win= Tk()
win.geometry('400x400')
# Declare an instance of canvas class
cnv = Canvas(win,height=300,width=300)
cnv.pack()
# This class takes threading as an argument
class FirstOval(Thread):
    def run(self):
        sleep(1)
        for i in range(1,4):
            # Create oval
            cnv.create_oval(10*i, 10*i, 100, 35*i,outline='blue',width=2)
            sleep(2)

class SecondOval(Thread):
    def run(self):
        sleep(1)
        for i in range(1,4):
            # Create oval
            cnv.create_oval(50*i, 10*i, 200, 35*i,outline='red',width=2)
            sleep(2)
# Create an object
first_oval=FirstOval()
first_oval.start()
second_oval=SecondOval()
second_oval.start()
win.mainloop()
'''
