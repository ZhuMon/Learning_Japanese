import random
import jp_listen
import ReuseChrome
import sys
import json

class RememberWord():
    def __init__(self, num_word = 20):
        self.num_word = num_word
        None

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
        t_num = 0 # true number
        wrong_ans = []

        for i in range(0, int(q_num)):

    def keyin(self):
        None

if __name__ == "__main__":
    func = RememberWord()
