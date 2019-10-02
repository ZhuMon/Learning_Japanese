from tkinter import *
from tkinter.ttk import *

from lib.MyTime import MyTime
from lib.number import MyNumber
from lib.fifty_symbol import FiftySymbol

class MainConsole(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent, width = 800, height=400)

        self.create_menubar("main")
        self.create_cframe()


        self.cframe.pack(fill="both")
        self.pack(fill="both")

    def create_cframe(self):
        self.cframe = Frame(self)
        ######## time ########
        self.time_frame = Frame(self.cframe)
        self.myTime = MyTime()
        self.myTime.q_var = StringVar()
        q_label = Label(self.time_frame, textvariable=self.myTime.q_var)
        
        self.myTime.a_var = StringVar()
        a_entry = Entry(self.time_frame, textvariable=self.myTime.a_var)

        self.myTime.t_a_var = StringVar()
        a_label = Label(self.time_frame, textvariable=self.myTime.t_a_var)
        
        enter_button = Button(self.time_frame, text = "Enter", command=self.test_time_compare)
        next_button = Button(self.time_frame, text = "Next", command=self.test_time_next)

    
        q_label.pack()
        a_entry.pack()
        enter_button.pack()
        a_label.pack()
        next_button.pack()

    def create_menubar(self, level = None):
        bar = Frame(self, width=800)
        buttons = []
        if level == "main":
            buttons = [
                ("Time",self.test_time),
                ("Number", self.test_number),
                ("FiftySymbol", self.test_50_symbol),
                ("Word", self.test_variable)
            ]

        if level != None:
            for name, cmd in buttons:
                b = Button(bar, text=name, command=cmd)
                b.pack(side='left')

        bar.pack(padx = 4, pady = 4, fill = 'none', expand=False, anchor='nw')

    def test_time(self):
        self.clear_widget(2)
        self.time_frame.pack()
        self.test_time_next()

    def test_time_next(self):
        r = next(self.myTime.start())
        
        q = r[0]
        self.time_ans = r[1]
        self.myTime.q_var.set(q)
        self.myTime.t_a_var.set("")

    def test_time_compare(self):
        if self.time_ans.replace(" ","") == self.myTime.a_var.get().replace(" ",""):
            self.myTime.t_a_var.set("True")
        else:
            self.myTime.t_a_var.set("False, the answer is "+self.time_ans)
        
        

    def test_number(self):
        MyNumber.start()

    def test_50_symbol(self):
        FiftySymbol.start()

    def test_variable(self):
        None

    def clear_widget(self, level = None):
        if level < 2:
            self.time_frame.pack_forget()

    def exit(self):
        self.myTime.stop()
    

if __name__ == "__main__":
    root = Tk()
    root.title( 'Learning Japanese' )
    root.geometry('800x400')
    main = MainConsole(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        main.exit()
