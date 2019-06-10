import dataModel


class Controller:
    def __init__(self, data: dataModel.DataModel):
        self._data: dataModel.DataModel = data

    def on_display_data_callback(self):
        self._data.open_relevant_data_view()

    def on_csv_file_selected(self, csv_file_path: str, replace_existing_data=False):
        self._data.load_csv_file(csv_file_path, replace_existing_data)
