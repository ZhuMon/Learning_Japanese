from tkinter import *
from tkinter.ttk import *
from functools import partial
import random

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

        ######## keyin frame ########
        self.key_in_frame = Frame(self.cframe)
        self.q_var = StringVar()
        q_label = Label(self.key_in_frame, textvariable=self.q_var)
        
        self.a_var = StringVar()
        a_entry = Entry(self.key_in_frame, textvariable=self.a_var)

        self.t_a_var = StringVar()
        a_label = Label(self.key_in_frame, textvariable=self.t_a_var)
        
        enter_button = Button(self.key_in_frame, text = "Enter", command=self.test_key_in_compare)
        next_button = Button(self.key_in_frame, text = "Next", command=self.test_key_in_next)

        
        q_label.pack()
        a_entry.pack()
        enter_button.pack()
        a_label.pack()
        next_button.pack()

        ######## choose frame ########
        self.choose_frame = Frame(self.cframe)
        q_label = Label(self.choose_frame, textvariable=self.q_var)
        
        self.a_ans_var = StringVar()
        self.b_ans_var = StringVar()
        self.c_ans_var = StringVar()
        self.d_ans_var = StringVar()
        a_button = Button(self.choose_frame, textvariable=self.a_ans_var, command=partial(self.test_choose_compare, self.a_ans_var))
        b_button = Button(self.choose_frame, textvariable=self.b_ans_var, command=partial(self.test_choose_compare, self.b_ans_var))
        c_button = Button(self.choose_frame, textvariable=self.c_ans_var, command=partial(self.test_choose_compare, self.c_ans_var))
        d_button = Button(self.choose_frame, textvariable=self.d_ans_var, command=partial(self.test_choose_compare, self.d_ans_var))

        next_button = Button(self.choose_frame, text = "Next", command=self.test_choose_next)
        a_label = Label(self.choose_frame, textvariable=self.t_a_var)

        q_label.pack()
        a_button.pack()
        b_button.pack()
        c_button.pack()
        d_button.pack()
        next_button.pack()
        a_label.pack()

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
        self.key_in_frame.pack()
        self.now_test = MyTime()
        self.test_key_in_next()

        
        

    def test_number(self):
        self.key_in_frame.pack()
        self.now_test = MyNumber()
        self.test_key_in_next()

    def test_50_symbol(self):
        self.choose_frame.pack()
        self.now_test = FiftySymbol()
        self.test_choose_next()

    def test_variable(self):
        None

    def test_key_in_next(self):
        r = next(self.now_test.start())
        
        q = r[0]
        self.ans = r[1]
        self.q_var.set(q)
        self.t_a_var.set("")

    def test_key_in_compare(self):
        if self.ans.replace(" ","") == self.a_var.get().replace(" ",""):
            self.t_a_var.set("True")
        else:
            self.t_a_var.set("False, the answer is "+self.ans)

    def test_choose_next(self):
        [q, self.ans, self.other_ans] = next(self.now_test.start())

        self.q_var.set(q)
        self.t_a_var.set("")
        ans_list = self.other_ans+[self.ans]
        random.shuffle(ans_list)
        self.a_ans_var.set(ans_list[0])
        self.b_ans_var.set(ans_list[1])
        self.c_ans_var.set(ans_list[2])
        self.d_ans_var.set(ans_list[3])


    def test_choose_compare(self, ans):
        if self.ans == ans.get():
            self.t_a_var.set("True")
        else:
            self.t_a_var.set("False, the answer is "+self.ans)

        # self.test_choose_next()

    def clear_widget(self, level = None):
        if level < 2:
            self.key_in_frame.pack_forget()

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
