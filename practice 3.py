from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")

def openNewWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow= Toplevel (window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    Label(newWindow, 
          text ="This is a new window").pack()


btn=Button(window,text="click me",command=openNewWindow)
btn.pack()


window.mainloop()