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
photo_best = PhotoImage(file = r"imgs/images.png")


better_label = ""


def showA():
    # get image and display
    image = PhotoImage(file = "imgs/A.png")
    imageLabel.configure(image = image)
    imageLabel.image = image


def showB():
    # get image and display
    image = PhotoImage(file = "imgs/B.png")
    imageLabel.configure(image = image)
    imageLabel.image = image

def getbestimage():
    global better_label
    global photo_best
    f = open("log.txt", "r")
    m_str = f.read()
    print(m_str)
    nums_as = m_str.count("A")
    nums_bs = m_str.count("B")
    print(nums_as)
    print(nums_bs)
    if nums_as >= nums_bs:
       showA()
    else:
        showB()

# Adding widgets to the root window
Label(root, text = 'cs260 mock webapp', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

  
# here, image option is used to
# set image on button
Button(root, text = 'Get better image',  command=getbestimage).pack(side = TOP)


imageLabel = Label(root)
imageLabel.pack(side=TOP)


root.mainloop()