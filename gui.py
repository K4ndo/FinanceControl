"""blabla class"""

import tkinter
import tkinter.filedialog as filedialog
from tkinter import Button
from tkinter import messagebox
import csv


class Gui:
    '''bla bla'''
    csv_data = None
    #root = None

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def start(self):
        '''seriously'''
        self.root = tkinter.Tk()
        self.add_gui_elements()
        self.root.mainloop()

    def add_gui_elements(self):
        "bla"
        tkinter.Label(self.root, text="Labeltext").grid(row=0)
        self.root.title("FinanceControl")
        actual_screenwidth = self.root.winfo_screenwidth()
        actual_screenheight = self.root.winfo_screenheight()
        x = (actual_screenwidth/2)-(self.width/2)
        y = (actual_screenheight/2)-(self.heigth/2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.heigth, x, y))
        self.root.grid_rowconfigure(4, minsize=100)
        tkinter.Label(self.root, text="Name").grid(row=1)
        tkinter.Entry(self.root).grid(row=1, column=1)
        tkinter.Label(self.root, text="Prename").grid(row=2)
        tkinter.Entry(self.root).grid(row=2, column=1)
        Button(self.root, text='Importiere neue CSV Datei',
               command=self.import_new_csv_data).grid(row=4, column=0)
        tkinter.Button(self.root, text='Arbeite mit bereites geladenen CSV Dateien',
                       command=self.show_csv_on_display).grid(row=4, column=1)
        tkinter.Button(self.root, text="Close", command=self.root.quit).grid(
            row=4, column=2)

    def set_label_name(self, name):
        """ b"""
        self.title = name

    def import_new_csv_data(self):
        ''''''
        self.csv_data = filedialog.askopenfilename(filetypes=(
            ("csv files", "*.csv"), ("all files", "*.*")))
        if self.csv_data:
            self.workOnlyWithNewCsvOrAddIt()

    def workOnlyWithNewCsvOrAddIt(self):
        choose_window = tkinter.Tk()
        choose_window.title("")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.heigth/2)
        choose_window.geometry('+%d+%d' % (x, y))
        tkinter.Button(
            choose_window, text="Mit aktueller CSV Datei arbeiten", command=(lambda a=True, f=choose_window: self.add_or_replace_csv_by_new_csv(f, a))).grid(column=0, row=0)
        tkinter.Button(
            choose_window, text="CSV Datei bestehenden Daten hinzufügen", command=(lambda a=False, f=choose_window: self.add_or_replace_csv_by_new_csv(f, a))).grid(column=1, row=0)

    def add_or_replace_csv_by_new_csv(self, frame, add=True):
        """"""
        frame.destroy()

    def show_csv_on_display(self):
        """"""
        if self.csv_data:
            root = tkinter.Tk()
            with open(self.csv_data, 'r') as csvfile:
                print(self.csv_data)
                reader = csv.reader(csvfile, delimiter=';')
                row_index = 0
                for row in reader:
                    col_index = 0
                    for col in row:
                        tkinter.Label(root, text=col).grid(
                            row=row_index, column=col_index)
                        col_index += 1
                    row_index += 1
        else:
            print(5)

    def testfunction(self):
        """"""
        if messagebox.askyesno('Verify', 'Really quit?'):
            messagebox.showwarning('Yes', 'Not yet implemented')
        else:
            messagebox.showinfo('No', 'Quit has been cancelled')


STARTING_GUI = Gui(800, 800)
STARTING_GUI.start()
#model = data_model(Gui.csvData)
