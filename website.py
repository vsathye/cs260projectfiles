import datetime
import time
import os
from tkhtmlview import HTMLLabel

from tkinter import * 
from tkinter.ttk import *


# creating tkinter window
root = Tk()

bg= Canvas(root, width = 400, height = 60, bg='white')
bg.pack()

f = open("log.txt", "w")
f.write("")
f.close()

def writeA():
    f = open("log.txt", "a")
    f.write("A")
    f.close()

def writeB():
    f = open("log.txt", "a")
    f.write("B")
    f.close()
# Adding widgets to the root window
Label(root, text = 'cs260 mock webapp', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"imgs/A.png")
  
# here, image option is used to
# set image on button
Button(root, text = 'Click Mekvjkhvjvh !', image = photo, command=writeA).pack(side = TOP)


label1 = Label(root, text= "tae anak kreante niyeay avei ampikhnhom  \nkaun nak kampoung te bn hlain aey")
bg.create_window(20, 40, window=label1)
# Creating a photoimage object to use image
photo2 = PhotoImage(file = r"imgs/B.png")
  
# here, image option is used to
# set image on button
Button(root, text = 'Click Me but again!', image = photo2, command=writeB).pack(side = TOP)


root.mainloop()