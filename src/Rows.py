from RowCategories import RowCategories


class Row:
    """classdoc"""
    def __init__(self, row_data):
        self.row_dict = {}
        self.parse_data_to_row_dict(row_data)

    def parse_data_to_row_dict(self, row_data):
        """bla"""
        if(len(row_data) is not len(RowCategories)):
            # exception
            raise Exception("Länge der eingegebenen Daten ist ungültig")
        for row_value, row_category in zip(row_data, RowCategories):
            self.row_dict[row_category.name] = row_value

    def get_auftragskonto(self):
        """lol"""
        return self.row_dict[RowCategories.AUFTRAGSKONTO.value]

    def get_buchungstag(self):
        """test"""
        return self.row_dict[RowCategories.BUCHUNGSTAG.value]

    def get_valutdatum(self):
        """test"""
        return self.row_dict[RowCategories.VALUTADATUM.value]

    def get_buchungstext(self):
        return self.row_dict[RowCategories.BUCHUNGSTAG.value]

    def get_verwendungszweck(self):
        return self.row_dict[RowCategories.VERWENDUNGSZWECK.value]

    def get_beguenstigter_zahlungspflichtiger(self):
        return self.row_dict[RowCategories.BEGUENSTIGTER_ZAHLUNGSPFLICHTIGER.value]

    def get_kontonummer(self):
        return self.row_dict[RowCategories.KONTONUMMER.value]

    def get_blz(self):
        return self.row_dict[RowCategories.BLZ.value]

    def get_betrag(self):
        return self.row_dict[RowCategories.BETRAG.value]

    def get_waehrung(self):
        return self.row_dict[RowCategories.WAEHRUNG.value]

    def get_info(self):
        return self.row_dict[RowCategories.INFO.value]
