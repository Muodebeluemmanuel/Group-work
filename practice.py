Igbo_dictionary = {"bia": 'come',
                   "eze": 'king',
                   "nri": 'food',
                   "isi": 'head',
                   "ire": 'tongue',
                   "onu": 'mouth',
                   "aka": 'hand',
                   "nkita": 'dog',
                   "agwa": 'beans',
                   "akpa": 'bag',
                   "nye": 'give/present',
                   "chineke": 'lord',
                   "ehi": 'cow',
                   "ewu": 'goat',
                   "ube": 'pear',
                   "imela": 'thank you',
                   "oyi": 'cold',
                   "ekpere": 'prayer',
                   "ego": 'money',
                   "chukwu": 'God'}
from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")


word = StringVar()
word_entry = Entry(window, textvariable=word, font=('ariel', 19))
word_entry.pack()


result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()


def search (word):
    if word in Igbo_dictionary:
        result.set(Igbo_dictionary[word])
        print(Igbo_dictionary[word])
    else:
        result.set("not found")


search_btn = Button(window, text="search", command=lambda: search(word.get()))
search_btn.pack()

Igbo_dictionarybt=Button(window,text="Igbo Dictionary",command=lambda: open("practice"))
Igbo_dictionarybt.pack()

exit_button=Button(window,text="exit",command=lambda: exit())
exit_button.pack()


word_entry = Entry(window, textvariable=word, font=('ariel', 19))
window.mainloop()

