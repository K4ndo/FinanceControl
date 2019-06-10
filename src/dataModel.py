import csv
from typing import List
import tkinter

import gui
from RowCategories import RowCategories
from Rows import Row


_RELEVANT_DATA_ROWS = [
    RowCategories.AUFTRAGSKONTO.value,
    RowCategories.BETRAG.value,
    RowCategories.BUCHUNGSTAG.value
]

class DataModel:
    ''''''

    def __init__(self, input_data=None):
        self.data = []
        if input_data:
            self.add_rows(input_data, 0)
        self._gui = None

    @property
    def relevant_data(self) -> List:
        relevant = []
        row_dictionaries = map(lambda row: row.row_dict, self.data)
        for row_dictionary in row_dictionaries:
            relevant_sub_dictionary = {k: v for k, v in row_dictionary.items() if k in _RELEVANT_DATA_ROWS}
            relevant.append(relevant_sub_dictionary)
        return relevant

    def set_view(self, main_gui: gui.Gui):
        """ Must be the first method called.
        """
        self._gui = main_gui

    def open_relevant_data_view(self):
        self._gui.display_data(self.relevant_data)

    def load_csv_file(self, csv_file_path: str, replace_existing_data=False):
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            if replace_existing_data:
                self.data.clear()
            self.add_rows(list(reader))

    def add_rows(self, csv_data: List, start_index=1):
        self.data.extend([Row(csv_row) for csv_row in csv_data[start_index:]])
