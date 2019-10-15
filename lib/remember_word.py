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

    def start(self, mode, listen):
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
            self.choose()
        elif mode == "b": # 問答
            self.keyin() 

    def choose(self): 
        """
        input:
        q_num : number of questions : type: (int)

        return:
        [question, answer, [opt1, opt2, opt3, opt4]]

        """
        t_num = 0 # true number
        wrong_ans = []

        while self.state :
            opt = random.sample(range(0, num_word), 4)
            ans_num = random.sample(opt, 1)  # true answer
            

            # question is chinese or japanese or ks(漢字)
            ch_or_jp = random.randint(0, 2)    # 0,1,2: jp, ch, ks
            
            # 0 -> 1; 1 -> 0 ; 2 -> 0,1
            another  = random.randint(0,1) if ch_or_jp == 2 else abs(ch_or_jp-1)
            question = self.word_list[ans_num].get(ch_or_jp)
            ans = self.word_list[ans_num].get(another)

            opt_list = [self.word_list[i].get(another) for i in opt]
            yield [question, ans, opt_list]

    def keyin(self):
        None

    def stop(self):
        self.state = False

if __name__ == "__main__":
    func = RememberWord()
