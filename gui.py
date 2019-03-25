import tkinter
import tkinter.filedialog

fields = {"a", "b", "c"}


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
            lab.setvar("test", 1)
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
    master = tkinter.Tk()
    master.geometry("500x500")
    ents = makeform(master, fields)
    #master.bind('<Return>', (lambda event, e=ents: fetch(e)))
    pathlabel = tkinter.Label(master)

    b1 = tkinter.Button(master, text='Show',
                        command=(lambda e=ents: fetch(e)))
    b1.pack(side=tkinter.LEFT, padx=5, pady=5)
    b2 = tkinter.Button(master, text='Quit', command=master.quit)
    b2.pack(side=tkinter.LEFT, padx=5, pady=5)
    b3 = tkinter.Button(master, text='browse', command=openFileDiaglogue)
    b3.pack(side=tkinter.LEFT, padx=5, pady=5)


master.mainloop()
