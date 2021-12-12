from tkinter import *
from tkinter import filedialog


note= Tk()
note.geometry("575x675")
note.title("Notepad")

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def clear():
    entry.delete(1.0,END)

def open_file():
    file = filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
        print(content)
    entry.insert(INSERT,content)

b1=Button(note,text="Salvar",command=save_file)
b1.place(x=10,y=10)

b2=Button(note,text="Apagar",command=clear)
b2.place(x=60,y=10)

b3=Button(note,text="Abrir",command=open_file)
b3.place(x=120,y=10)

entry=Text(note,height=33, width=58, font=("Open Sans", 12), wrap=WORD)
entry.place(x=10,y=50)

note.mainloop()