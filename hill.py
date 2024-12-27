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

Igala_dictionary={"gba":'take',
                "oskapa":'rice',
                "Oji":'head',
                "eju":'face',
                "efu":'stomach',
                "ehi":'cook',
                "adide":'guard',
                "ojika":'shoulder',
                "okwukwu":'kneel',
                "nalo":'go',
                "ubi":'back',
                "imi":'breath',
                "imo":'nose',
                "unyi":'house',
                "ule era":'run',
                "omi":'fish',
                "eti":'ear',
                "oli":'tree',
                "l'olu":'sleep'}
from tkinter import Tk, Entry, Button, Label, StringVar,Menubutton,Menu

window = Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")



def openNewWindow():
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

def Igala():
     word = StringVar()
     word_entry = Entry(window, textvariable=word, font=('ariel', 19))
     word_entry.pack()


     result = StringVar()
     result_label = Label(window, textvariable=result)
     result_label.pack()


     def search (word):
        if word in Igala_dictionary:
            result.set(Igala_dictionary[word])
            print(Igala_dictionary[word])
        else:
            result.set("not found")
            
     search_btn = Button(window, text="search", command=lambda: search(word.get()))
     search_btn.pack()

menu1_btn=Button(window,text="Igbo Language",command=(openNewWindow))
menu1_btn.pack() 

menu2_btn=Button(window,text="Igala Language",command=(Igala))
menu2_btn.pack() 


window.mainloop()

