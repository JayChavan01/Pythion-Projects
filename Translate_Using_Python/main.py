#pip install googletrans

#importing the tkinter modules


from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


# #Define Functions....

def change(text = "type", src = "English", dest = "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate (text, src = src1, dest = dest1)
    return trans1.text

def data():
    s = comb_Ent.get()
    d = comb_Trans.get()
    masg = Ent_txt.get(1.0, END)
    Textget = change(text = masg, src = s, dest = d)
    Trans_txt.delete (1.0, END)
    Trans_txt.insert (END,Textget)

   
# # GUI Code ...
root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg="Black")
# root.resizable(0,0)


lab_txt = Label (root, text = "Translator", font = ("Time New Roman", 40, "bold"),fg = "Sky Blue", bg = "Black")
lab_txt.place (x=100, y=40, height=50, width=300)


frame = Frame (root).pack (side = BOTTOM)


lab_txt = Label (root, text = "Enter Text", font = ("Time New Roman", 20, "bold"), fg = "White", bg = "Black")
lab_txt.place  (x=100, y=100, height=20, width=300)


Ent_txt = Text (frame, font = ("Time New Roman", 12),wrap=WORD)
Ent_txt.place (x=10, y=130, height=150, width = 480)


list_text = list (LANGUAGES.values())


comb_Ent = ttk.Combobox(frame, values = list_text)
comb_Ent.place(x=10, y=300, height=40, width = 150)
comb_Ent.set ("English")


button_change = Button (frame, text = "Translate", relief=RAISED, command = data)
button_change.place  (x=175, y=300, height=40, width=150)


comb_Trans= ttk.Combobox(frame, values = list_text)
comb_Trans.place(x=340, y=300, height=40, width = 150)
comb_Trans.set ("English")


lab_txt = Label (root, text = "Translation", font = ("Time New Roman", 20, "bold"), fg="White", bg = "Black")
lab_txt.place  (x=100, y=360, height=20, width=300)

Trans_txt = Text (frame, font = ("Time New Roman", 12), wrap = WORD)
Trans_txt.place (x=10, y=400, height=150, width = 480)


root.mainloop()