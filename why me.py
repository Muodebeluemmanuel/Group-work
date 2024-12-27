Igbo_dictionary={"bia":'come',
            "eze":'king',
            "nri":'food',
            "isi":'head'}
from tkinter import  Tk, Entry, Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")

word=StringVar()
word_label=Label(window,text="word",font=('ariel',10))
word_entry=Entry(word_label,font=('ariel',19))
 