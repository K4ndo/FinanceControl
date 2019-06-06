# monatliche Ausgaben
import csv
from enum import Enum

class Spalte(Enum):

    transactionDate = 1
    Beguenstigter  = 2
    Betrag = 3


with open('file.CSV', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ';')
    keylist = ["AMAZON", "LIDL","NETFLIX", "LIFEPARK", "EDEKA",  "NOTEBOOKSBI", "MARKTKAUF", "TAKEAWAY", "NETTO", "ALDI"]
    csvdata_Fix  = [[]  for _ in keylist]
    for row in spamreader:
        for index, key in enumerate(keylist):
            if  key in row[5]:
                coloumn_five_and_six = [row[4].lstrip('"').rstrip('"')+ ' ',row[5].lstrip('"').rstrip('"')+ ' ', row[8].lstrip('"').rstrip('"')+ ' ']
                csvdata_Fix[index].append(coloumn_five_and_six )
                
        

with open('ergebnis.csv', 'w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar =';')
    spamwriter.writerow(['Fixkosten ', 'Privatvergnügen ', 'notwendig ', 'sontige '])
    for index, row in enumerate(csvdata_Fix):
        for innerRow in csvdata_Fix[index]:
            spamwriter.writerow(innerRow)


def sort_function(list, Order):
    i = 5
    print(i)

def erzeugeEinnahmenAusgaben(csv):
    einnahmen = []
    ausgaben = []
    for row in csv:
        if float(row[Spalte.Betrag]) >= 0:
            einnahmen.append(row)
        else:
            ausgaben.append(row)
    print("test")


    

        




