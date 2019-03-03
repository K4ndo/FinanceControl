from tkinter import*
from tkinter import filedialog
# def show_entry_fields():
#   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

'''
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1.delete(0, END)
    e2.delete(0, END)
'''


def NewFile():
    print("New File!")


def OpenFile():
    print("name")


fields = "Vorname", "Nachname", "Kontoauszug"


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))
        openFileDiaglogue()


def makeform(root, fields):
    entries = []
    for field in fields:
        frame = Frame(root)
        lab = Label(frame, width=25, text=field, anchor='w', justify=LEFT)
        ent = Entry(frame, justify=LEFT)
        b1 = Button(frame, text='browse',
                    command=(openFileDiaglogue))
        frame.pack(side=TOP, fill=NONE, padx=10, pady=10)
        lab.pack(side=LEFT)
        #ent.pack(side=LEFT, expand=YES, fill=X)
        ent.pack(side=LEFT)

        if field is fields[2]:
            # entries.append((field, ent))
            b1.pack(expand=YES, fill=X)
        entries.append((field, ent))

    return entries


def openFileDiaglogue():

    file = filedialog.askopenfile(
        parent=master, mode='rb', title='Choose a file')
    pathlabel.config(text=file)
    pathlabel.pack()
    print(file.name)
    if file != None:
        data = file.read()
        file.close()
        print("I got %d bytes from this file." % len(data))


if __name__ == '__main__':
    master = Tk()
    master.geometry("500x500")
    ents = makeform(master, fields)
    #master.bind('<Return>', (lambda event, e=ents: fetch(e)))
    pathlabel = Label(master)

    b1 = Button(master, text='Show',
                command=(lambda e=ents: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(master, text='Quit', command=master.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(master, text='browse', command=openFileDiaglogue)
    b3.pack(side=LEFT, padx=5, pady=5)


'''
root.mainloop()
'''
'''
master = Tk()
master.title("Finance Controle")
menubar = Menu(master)
master.config(menu=menubar)
filemenu = Menu(menubar)
'''

'''
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
'''

'''
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Speichtern unter", command=NewFile())
# filemenu.add_separator()
filemenu.add_command(label="Programm beenden", command=OpenFile())
master.geometry("400x200")

Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label()
e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
test = e1.get()

Button(master, text='Quit', command=master.quit).grid(
    row=3, column=0, sticky=W, pady=4)

Button(master, text='Show', command=openFileDiaglogue()).grid(
    row=3, column=1, sticky=W, pady=4)
'''

#Button(master, text='Show', command=openFileDiaglogue())


master.mainloop()
