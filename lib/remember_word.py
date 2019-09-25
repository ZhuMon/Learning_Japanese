import random
import jp_listen
import ReuseChrome
import sys
import json

class RememberWord():
    def __init__(self, word_list = None, num_word = 20):
        """
        word_list = [obj1, obj2, ...]
        obj1 = Word()
        Word.jp Word.ch Word.ks Word.n
        """
        self.word_list = word_list
        self.num_word = num_word

    def start(self, mode, q_num, listen):
        if listen == True:
            try:
                web_id = open('id', 'r')
                executor_url = ''
                session_id = ''
                executor_url = web_id.readline().strip()
                session_id = web_id.readline().strip()

                if executor_url != '' and session_id != '':
                    self.driver = ReuseChrome.ReuseChrome(command_executor = executor_url, session_id = session_id)
                else:
                    self.driver = jp_listen.openweb()
            except FileNotFoundError:
                self.driver = jp_listen.openweb()
        
        if mode == "a": # 選擇
            self.choose(q_num)
        elif mode == "b": # 問答
            self.keyin() 

    def choose(self, q_num): 
        """
        input:
        q_num : number of questions : type: (int)

        return:
        {question1:[answer, opt1, opt2, opt3], q2:...} 

        """
        t_num = 0 # true number
        wrong_ans = []
        out = {}

        for i in range(0, int(q_num)):
            opt = random.sample(range(0, num_word), 4)
            num = random.sample(opt, 1)  # true answer
            
            out[self.word_list[num].jp] = []

            # question is chinese or japanese
            ch_or_jp = random.randint(0, 2)    
            another  = 0 if ch_or_jp>0 else 1

            ans = -1
            which_opt = random.randint(0, 3)
            
    def keyin(self):
        None

if __name__ == "__main__":
    func = RememberWord()
