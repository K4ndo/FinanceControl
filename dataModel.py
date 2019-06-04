import tkinter
from RowCategories import RowCategories
from Rows import Row


class DataModel:
    ''''''
    relevant_data = [RowCategories.AUFTRAGSKONTO.value,
                     RowCategories.BETRAG.value, RowCategories.BUCHUNGSTAG.value]

    def __init__(self, input_data=None):
        self.data = []
        if input_data:
            self.add_rows(input_data, 0)

    def add_rows(self, csv_data, start_index=1):
        for csv_row in csv_data[start_index:]:
            self.data.append(Row(csv_row))

        print(self.data)

    def show_relevant_data(self):
        ''' blub'''
        root = tkinter.Tk()
        row_index = 0
        for data_row in self.data:
            col_index = 0
            for data_col_key, data_col_value in data_row.row_dict.items():
                if data_col_key in self.relevant_data:
                    tkinter.Label(root, text=data_col_value).grid(
                        row=row_index, column=col_index, padx=5)
                    col_index += 2
            row_index += 1
