import tkinter
import tkinter.filedialog as filedialog
from tkinter import Button
from tkinter import messagebox
import csv


class Gui:

    csvData = None

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def start(self):
        self.root = tkinter.Tk()
        self.guiInit()
        self.root.mainloop()

    def guiInit(self):
        tkinter.Label(self.root, text="Labeltext").grid(row=0)
        self.root.title("FinanceControl")
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2)-(self.width/2)
        y = (hs/2)-(self.heigth/2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.heigth, x, y))
        self.root.grid_rowconfigure(4, minsize=100)
        tkinter.Label(self.root, text="Name").grid(row=1)
        tkinter.Entry(self.root).grid(row=1,  column=1)
        tkinter.Label(self.root, text="Prename").grid(row=2)
        tkinter.Entry(self.root).grid(row=2,  column=1)
        tkinter.Button(self.root, text='Importiere neue CSV Datei',
                       command=self.importNewCsvData).grid(row=4, column=0)
        tkinter.Button(self.root, text='Arbeite mit bereites geladenen CSV Dateien',
                       command=self.showCsvOnDisplay).grid(row=4, column=1)
        tkinter.Button(self.root, text="Close", command=self.root.quit).grid(
            row=4, column=2)

    def setLabelName(self, name):
        self.title = name

    def indexRowAndIncrease(self, oldRowIndex):
        '''returns the actual index of the row in the grid and increases it by 1'''

        rowIndex = oldRowIndex + 1
        return rowIndex

    def indexColumnAndIncrease(self, oldColumnIndex):
        '''returns the actual index of the column in the grid and increases it by 1'''

        columnIndex = oldColumnIndex + 1
        return columnIndex

    def importNewCsvData(self):
        ''' '''
        self.csvData = filedialog.askopenfilename(filetypes=(
            ("csv files", "*.csv"), ("all files", "*.*")))
        if self.csvData:
            self.workOnlyWithNewCsvOrAddIt()

    def workOnlyWithNewCsvOrAddIt(self):
        chooseWindow = tkinter.Tk()
        chooseWindow.title("")
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        x = (screenWidth/2) - (self.width/2)
        y = (screenHeight/2) - (self.heigth/2)
        chooseWindow.geometry('+%d+%d' % (x, y))
        tkinter.Button(
            chooseWindow, text="Mit aktueller CSV Datei arbeiten",  command=(lambda a=True, f=chooseWindow: self.addOrReplaceCsvByNewCSV(f, a))).grid(column=0, row=0)
        tkinter.Button(
            chooseWindow, text="CSV Datei bestehenden Daten hinzufügen",  command=(lambda a=False, f=chooseWindow: self.addOrReplaceCsvByNewCSV(f, a))).grid(column=1, row=0)

    def addOrReplaceCsvByNewCSV(self, frame, add=True):
        frame.destroy()

    def showCsvOnDisplay(self):
        if self.csvData:
            root = tkinter.Tk()
            with open(self.csvData, 'r') as csvfile:
                print(self.csvData)
                reader = csv.reader(csvfile, delimiter=';')
                rowIndex = 0
                for row in reader:
                    colIndex = 0
                    for col in row:
                        tkinter.Label(root, text=col).grid(
                            row=rowIndex, column=colIndex)
                        colIndex += 1
                    rowIndex += 1
        else:
            print(5)

    def testfunction(self):
        if messagebox.askyesno('Verify', 'Really quit?'):
            messagebox.showwarning('Yes', 'Not yet implemented')
        else:
            messagebox.showinfo('No', 'Quit has been cancelled')


startingGui = Gui(800, 800)
startingGui.start()
