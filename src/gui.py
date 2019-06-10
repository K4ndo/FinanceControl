"""blabla class"""

from typing import Dict
from typing import List

import tkinter
import tkinter.filedialog as filedialog
from tkinter import Button
from tkinter import messagebox
import csv

from RowCategories import RowCategories


class Gui:
    '''bla bla'''

    csv_data = None
    data_model = None

    def __init__(self, width: int, heigth: int, ctr: "Controller"):
        self.width = width
        self.heigth = heigth
        self._ctr = ctr

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
               command=self.open_csv_import_dialog).grid(row=4, column=0)
        tkinter.Button(self.root, text='Arbeite mit bereites geladenen CSV Dateien',
                       command=self._ctr.on_display_data_callback).grid(row=4, column=1)
        tkinter.Button(self.root, text="Close", command=self.root.quit).grid(
            row=4, column=2)

    def set_label_name(self, name):
        """ b"""
        self.title = name

    def open_csv_import_dialog(self):
        ''''''
        csv_file = filedialog.askopenfilename(filetypes=(
            ("csv files", "*.csv"), ("all files", "*.*")))
        if csv_file:
            # FIXME: Make this a checkbox and pass parameter replace_existing_data:bool to self._ctr.on_csv_file_selected
            self.workOnlyWithNewCsvOrAddIt(csv_file)

    def workOnlyWithNewCsvOrAddIt(self, csv_file):
        choose_window = tkinter.Tk()
        choose_window.title("")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.heigth/2)
        choose_window.geometry('+%d+%d' % (x, y))
        tkinter.Button(
            choose_window, text="Mit aktueller CSV Datei arbeiten", command=(lambda: self.add_or_replace_data_in_data_model(choose_window, csv_file, True))).grid(column=0, row=0)
        tkinter.Button(
            choose_window, text="CSV Datei bestehenden Daten hinzufügen", command=(lambda: self.add_or_replace_data_in_data_model(choose_window, csv_file, False))).grid(column=1, row=0)

    def add_or_replace_data_in_data_model(self, frame, csv_file, replace_existing_data):
        """"""
        self._ctr.on_csv_file_selected(csv_file, replace_existing_data)
        frame.destroy()

    def display_data(self, data: List[Dict]):
        root = tkinter.Tk()
        for row_index, data_row in enumerate(data):
            # FIXME: This won't work, since order in a dict isn't guaranteed.
            for col_index, data_col_value in enumerate(data_row.values()):
                tkinter.Label(root, text=data_col_value).grid(
                    row=row_index, column=col_index*2, padx=5)
