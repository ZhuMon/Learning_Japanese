from tkinter import *
from tkinter.ttk import *

from MyTime import MyTime

class MainConsole(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)


    def create_menubar(self, level = None):
        None

    def time(self):
        MyTime.start()

    def clear_widget(self, level = None):
        None

    

if __name__ == "__main__":
    root = Tk()
    MainConsole(root)
    
    root.mainloop()

