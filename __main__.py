from tkinter import *
from tkinter.ttk import *

from lib.MyTime import MyTime
from lib.number import MyNumber
from lib.fifty_symbol import FiftySymbol

class MainConsole(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)


    def create_menubar(self, level = None):
        None

    def test_time(self):
        MyTime.start()

    def test_number(self):
        MyNumber.start()

    def test_50_symbol(self):
        FiftySymbol.start()

    def test_variable(self):
        None

    def clear_widget(self, level = None):
        None

    

if __name__ == "__main__":
    root = Tk()
    MainConsole(root)
    
    root.mainloop()

