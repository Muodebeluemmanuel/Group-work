#tuple are immutable(cannot be change)
my_tuple=(-1,7,6,9)
Igbo_dictionary={"bia":'come',
            "eze":'king',
            "nri":'food',
            "isi":'head'}

yoruba_dictionary={"zo":'come'}

from tkinter import  Tk, Entry, Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")

Igbo_dictionary=StringVar
def open():
    open(Igbo_dictionary)

Igbo_dictionary_button=Button(window,text="Igbo_dictionary",command=lambda: open(Igbo_dictionary_button))
Igbo_dictionary_button.pack()

def open():
    open(yoruba_dictionary)


word=StringVar()
entry_text=Entry(window,textvariable=word, font=('calibre',10,'normal'))
entry_text.pack()

result=StringVar()
result_label=Label(window, textvariable=result)
result_label.pack()

def search(word):
    if word in Igbo_dictionary:
        result.set(Igbo_dictionary[word])
        print(Igbo_dictionary[word])
    else:
        result.set("not found")


search_btn=Button(window, text="search",command=lambda: search(word.get()))
search_btn.pack()

entry_text=Entry(window,textvariable=word, font=('calibre',10,'normal'))
window.mainloop()