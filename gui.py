from tkinter import*

from tkinter import filedialog

#def show_entry_fields():
#   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def NewFile():
   print ("New File!")
def OpenFile():
   print("name")

master = Tk()
master.title("Finance Controle")
menubar = Menu(master)
master.config(menu=menubar)
filemenu = Menu(menubar)
'''
def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
'''
filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Speichtern unter", command = NewFile())
#filemenu.add_separator()
filemenu.add_command(label="Programm beenden", command = OpenFile())
'''
menubar.add_cascade(label = "Datei", menu=filemenu)

editmenu = Menu(menubar, tearoff= 0)
editmenu.add_command(label ="Rückgängig", command = undo)
editmenu.add_separator()
editmenu.add_command(label="Wiederholen", command = redo)
menubar.add_cascade(label="Bearbeiten", menu= editmenu)
'''
master.config(menu = menubar)
master.mainloop()
'''
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
'''