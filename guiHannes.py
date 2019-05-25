# from tkinter import* # FIXME keine Wildcard imports
import tkinter
import tkinter.filedialog


def _print_entered_data(field_names_and_entries):
    for field_name in field_names_and_entries.keys():
        text = field_names_and_entries[field_name].get()
        print('{}: "{}"'.format(field_name, text))


def _create_entry_row(root, name, with_browse_button=False):
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.TOP, fill=tkinter.X, padx=10, pady=10)

    field_name_label = tkinter.Label(
        frame, width=25, text=name, anchor='w', justify=tkinter.LEFT)
    field_name_label.pack(anchor=tkinter.W, side=tkinter.LEFT)

    entry = tkinter.Entry(frame, justify=tkinter.LEFT)
    entry.pack(anchor=tkinter.W, side=tkinter.LEFT, fill=tkinter.X)

    if with_browse_button:
        browse_button = tkinter.Button(
            frame, text='browse', command=_open_file_dialog)
        browse_button.pack(anchor=tkinter.W)
    return entry


def _make_form(root):
    field_names_and_entries = {}
    first_name = "Vorname"
    field_names_and_entries[first_name] = _create_entry_row(root, first_name)
    last_name = "Nachname"
    field_names_and_entries[last_name] = _create_entry_row(root, last_name)
    statement_path = "Kontoauszug"
    field_names_and_entries[statement_path] = _create_entry_row(
        root, statement_path, with_browse_button=True)
    return field_names_and_entries


def _open_file_dialog():
    # FIXME Niemals eine Variable "file" nennen (ist ein Python-Keyword)
    chosen_file = tkinter.filedialog.askopenfile(
        parent=master, mode='rb', title='Choose a file')
    pathlabel.config(text=chosen_file)
    pathlabel.pack()
    if chosen_file:
        print(chosen_file.name)
        # FIXME data sollte dann wohl in eine globale Variable, oder (wenn du das ganze in einer Klasse schreibst) in eine Klassenvariable
        data = chosen_file.read()
        chosen_file.close()
        print("I got %d bytes from this file." % len(data))


if __name__ == '__main__':
    master = tkinter.Tk()
    master.geometry("500x200")

    entries = _make_form(master)
    pathlabel = tkinter.Label(master)

    b1 = tkinter.Button(master, text='Show', command=(
        lambda e=entries: _print_entered_data(e)))
    b1.pack(side=tkinter.LEFT, padx=5, pady=5)
    b2 = tkinter.Button(master, text='Quit', command=master.quit)
    b2.pack(side=tkinter.LEFT, padx=5, pady=5)
    b3 = tkinter.Button(master, text='browse', command=_open_file_dialog)
    b3.pack(side=tkinter.LEFT, padx=5, pady=5)

    master.mainloop()
