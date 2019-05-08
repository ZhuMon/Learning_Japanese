import random
import jp_listen
import ReuseChrome
import sys
import json

word_key = ['jp', 'ch', 'ks_bool', 'ks', 'aw_bool', 'aw_jp', 'aw_ks_bool', 'aw_ks']

infile = open('json_phrases', 'r')
"""
word_list = []
line_list = []
all_word_list = []

content = infile.read()
line_list = content.splitlines(False)

for i in range(0, len(line_list)):
    word_list = line_list[i].split('\t')
    all_word_list.append(word_list) 
"""
all_word_list = []
file_data = infile.readline()
while file_data:
    json_data = json.loads(file_data)
    all_word_list.append(json_data)
    file_data = infile.readline()

mode = input("Which mode? (選擇題(a) 問答題(b)) ")
q_num = input("How many questions? ") # question number


try:
    web_id = open('id', 'r')
    executor_url = ''
    session_id = ''
    executor_url = web_id.readline().strip()
    session_id = web_id.readline().strip()

    if executor_url != '' and session_id != '':
        driver = ReuseChrome.ReuseChrome(command_executor=executor_url, session_id=session_id)
    else:
        driver = jp_listen.openweb()
except FileNotFoundError:
    driver = jp_listen.openweb()

if mode is 'a':
    t_num = 0; # true number
    wrong_ans = []


    for i in range(0, int(q_num)):
        num = random.randint(0, len(all_word_list)-1)

        testable = [0, 1, 3, 5, 7]

        if all_word_list[num]['ks_bool'] == "0":
            testable.remove(3)
        if all_word_list[num]['aw_bool'] == "0":
            testable.remove(5)
        if all_word_list[num]['aw_ks_bool'] == "0":
            testable.remove(7)
        #print(testable)
        type_to_test = random.choice(testable)
        an_ttt = -1 #another_type_to_test

        if type_to_test == 0: # jp
            if all_word_list[num]['aw_ks_bool'] == "1":
                an_ttt = random.choice([1, 5, 7]) # ch, aw_jp, aw_ks
            elif all_word_list[num]['aw_bool'] == "1":
                an_ttt = random.choice([1, 5]) # ch, aw_jp
            else:
                an_ttt = 1
        elif type_to_test == 1: # ch
            if all_word_list[num]['ks_bool'] == "1":
                an_ttt = random.choice([0, 3]) # jp, ks
            else:
                an_ttt = 0
        elif type_to_test == 3: # ks
            if all_word_list[num]['aw_ks_bool'] == "1":
                an_ttt = random.choice([1, 5, 7]) # ch, aw_jp, aw_ks
            elif all_word_list[num]['aw_bool'] == "1":
                an_ttt = random.choice([1, 5]) # ch, aw_jp
            else:
                an_ttt = 1
        elif type_to_test == 5: # aw_jp
            if all_word_list[num]['ks_bool'] == "1":
                an_ttt = random.choice([0, 3]) # jp, ks
            else:
                an_ttt = 0
        elif type_to_test == 7: # aw_ks
            if all_word_list[num]['ks_bool'] == "1":
                an_ttt = random.choice([0, 3]) # jp, ks
            else:
                an_ttt = 0

        if an_ttt == -1:
            sys.exit("an_ttt error")

        wrong1 = random.randint(0, len(all_word_list)-1)
        while wrong1 == num or (an_ttt == 5 and all_word_list[num]['aw_jp'] == all_word_list[wrong1]['jp']) or (an_ttt == 7 and all_word_list[num]['aw_ks'] == all_word_list[wrong1]['ks']):
            wrong1 = random.randint(0, len(all_word_list)-1)

        wrong2 = random.randint(0, len(all_word_list)-1)
        while wrong2 == num or wrong2 == wrong1 or (an_ttt == 5 and all_word_list[num]['aw_jp'] == all_word_list[wrong2]['jp']) or (an_ttt == 7 and all_word_list[num]['aw_ks'] == all_word_list[wrong2]['ks']):
            wrong2 = random.randint(0, len(all_word_list)-1)

        wrong3 = random.randint(0, len(all_word_list)-1)
        while wrong3 == num or wrong3 == wrong1 or wrong3 == wrong2 or (an_ttt == 5 and all_word_list[num]['aw_jp'] == all_word_list[wrong3]['jp']) or (an_ttt == 7 and all_word_list[num]['aw_ks'] == all_word_list[wrong3]['ks']):
            wrong3 = random.randint(0, len(all_word_list)-1)
        
        opt = [num, wrong1, wrong2, wrong3]


        print(str(i+1)+'. '+ all_word_list[num][word_key[type_to_test]])
        #print(str(num) + " " + str(type_to_test))
        ans = -1

        which_opt = random.randint(0, 3)
        which_word = opt.pop(which_opt)
        opt_appear = all_word_list[which_word][word_key[an_ttt]]
        if type_to_test == 0 or type_to_test == 3:
            if an_ttt == 5:
                opt_appear = all_word_list[which_word]['jp']
            elif an_ttt == 7: 
                if all_word_list[which_word]['ks_bool'] == "1":
                    opt_appear = all_word_list[which_word]['ks']
                else:
                    opt_appear = all_word_list[which_word]['jp']
        elif (type_to_test == 1 or type_to_test == 5 or type_to_test == 7) and an_ttt == 3 and all_word_list[which_word]['ks_bool'] == "0":
            opt_appear = all_word_list[which_word]['jp']


        print("   (1) " + opt_appear+' ')
        if ans == -1 and which_opt == 0:
            ans = 0

        which_opt = random.randint(0, 2)
        which_word = opt.pop(which_opt)
        opt_appear = all_word_list[which_word][word_key[an_ttt]]
        if type_to_test == 0 or type_to_test == 3:
            if an_ttt == 5:
                opt_appear = all_word_list[which_word]['jp']
            elif an_ttt == 7: 
                if all_word_list[which_word]['ks_bool'] == "1":
                    opt_appear = all_word_list[which_word]['ks']
                else:
                    opt_appear = all_word_list[which_word]['jp']
        elif (type_to_test == 1 or type_to_test == 5 or type_to_test == 7) and an_ttt == 3 and all_word_list[which_word]['ks_bool'] == "0":
            opt_appear = all_word_list[which_word]['jp']

        print("   (2) " + opt_appear+' ')
        if ans == -1 and which_opt == 0:
            ans = 1


        which_opt = random.randint(0, 1)
        which_word = opt.pop(which_opt)
        opt_appear = all_word_list[which_word][word_key[an_ttt]]
        if type_to_test == 0 or type_to_test == 3:
            if an_ttt == 5:
                opt_appear = all_word_list[which_word]['jp']
            elif an_ttt == 7: 
                if all_word_list[which_word]['ks_bool'] == "1":
                    opt_appear = all_word_list[which_word]['ks']
                else:
                    opt_appear = all_word_list[which_word]['jp']
        elif (type_to_test == 1 or type_to_test == 5 or type_to_test == 7) and an_ttt == 3 and all_word_list[which_word]['ks_bool'] == "0":
            opt_appear = all_word_list[which_word]['jp']

        print("   (3) " + opt_appear+' ')
        if ans == -1 and which_opt == 0:
            ans = 2

        which_opt = 0
        which_word = opt.pop(which_opt)
        opt_appear = all_word_list[which_word][word_key[an_ttt]]
        if type_to_test == 0 or type_to_test == 3:
            if an_ttt == 5:
                opt_appear = all_word_list[which_word]['jp']
            elif an_ttt == 7: 
                if all_word_list[which_word]['ks_bool'] == "1":
                    opt_appear = all_word_list[which_word]['ks']
                else:
                    opt_appear = all_word_list[which_word]['jp']
        elif (type_to_test == 1 or type_to_test == 5 or type_to_test == 7) and an_ttt == 3 and all_word_list[which_word]['ks_bool'] == "0":
            opt_appear = all_word_list[which_word]['jp']
        
        print("   (4) " + opt_appear+'\n')
        if ans == -1 and which_opt == 0:
            ans = 3
        
        feedback = input("   ")
        if int(feedback)-1 == ans:
            t_num = t_num + 1
            print("\n   True")
            jp_listen.speak(driver, all_word_list[num]['jp'], False, 4)
            if an_ttt > 5:
                jp_listen.speak(driver, all_word_list[num]['aw_jp'], False, 4)

            print("----------------")
        else:
            print("\n   False")
            print("   Ans is " + all_word_list[num][word_key[an_ttt]])
            jp_listen.speak(driver, all_word_list[num]['jp'], False, 4)
            if an_ttt > 4:
                jp_listen.speak(driver, all_word_list[num]['aw_jp'], False, 4)

            # swap
            if type_to_test > 4:
                a_wrong_ans = [num, an_ttt, type_to_test]
            elif type_to_test == 1 and (an_ttt == 3 or an_ttt == 0):
                a_wrong_ans = [num, an_ttt, type_to_test]
            else: 
                a_wrong_ans = [num, type_to_test, an_ttt]

            wrong_ans.append(a_wrong_ans)
            print("----------------")

    print("Score: " + str(t_num) + '/' + q_num)
    if t_num != int(q_num):
        print("Wrong answer: ")
        for i in range(0, int(q_num)-t_num):
            a_wrong_ans = wrong_ans.pop(0)
            print(all_word_list[a_wrong_ans[0]][word_key[a_wrong_ans[1]]] + '\t' + all_word_list[a_wrong_ans[0]][word_key[a_wrong_ans[2]]])

elif mode is 'b':
    wk_mode = input("Write or key in? (write(w) key in(k)) ")
    if wk_mode is 'w':
        for i in range(0, int(q_num)-1 ):
            num = random.randint(0, len(all_word_list)-1)
            ch_or_jp = random.randint(0, 1)
            another  = 1 - ch_or_jp
            
            print(str(i+1) + ". " + all_word_list[num][ch_or_jp])
            input()
            print(all_word_list[num][another])
            jp_listen.speak(driver, all_word_list[num][0], False, 4)
            print("----------------")

    elif wk_mode is 'k':
        t_num = 0
        wrong_ans = []
        for i in range(0, int(q_num) ):
            num = random.randint(0, len(all_word_list)-1)
            print(str(i+1) + ". " + all_word_list[num][1])
            feedback = input("   日文： ")
            if feedback == all_word_list[num][0]:
                print("\n   True")
                t_num = t_num + 1
            else:
                print("\n   False")
                wrong_ans.append(num)
                print("   Ans : " + all_word_list[num][0])
            
            jp_listen.speak(driver, all_word_list[num][0], False, 4)
            print("----------------")

        print("Score: " + str(t_num) + '/' + q_num)
        if t_num != int(q_num):
            print("Wrong answer: ")
            for i in range(0, int(q_num)-t_num):
                num = wrong_ans.pop(0)
                print(all_word_list[num][0] + '\t' + all_word_list[num][1])
            

cont_web = input("Do you continue to learn? Yes(y)/No(n) ")
web_id_w = open('id', 'w')
if cont_web is 'y':
    web_id_w.write(driver.command_executor._url+'\n')
    web_id_w.write(driver.session_id + '\n')
    web_id_w.close()
    #del driver
else:
    driver.quit()

