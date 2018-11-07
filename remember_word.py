import random
import jp_listen
import ReuseChrome

infile = open('words', 'r')

word_list = []
line_list = []
all_word_list = []

content = infile.read()
line_list = content.splitlines(False)

for i in range(0, len(line_list)):
    word_list = line_list[i].split('\t')
    all_word_list.append(word_list) 


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
        wrong1 = random.randint(0, len(all_word_list)-1)
        while wrong1 == num:
            wrong1 = random.randint(0, len(all_word_list)-1)

        wrong2 = random.randint(0, len(all_word_list)-1)
        while wrong2 == num or wrong2 == wrong1:
            wrong2 = random.randint(0, len(all_word_list)-1)

        wrong3 = random.randint(0, len(all_word_list)-1)
        while wrong3 == num or wrong3 == wrong1 or wrong3 == wrong2:
            wrong3 = random.randint(0, len(all_word_list)-1)
        
        opt = [num, wrong1, wrong2, wrong3]

        ch_or_jp = random.randint(0, 1)
        another  = 1 - ch_or_jp

        print(str(i+1)+'. '+ all_word_list[num][ch_or_jp])
        ans = -1
        which_opt = random.randint(0, 3)
        print("   (1) " + all_word_list[opt.pop(which_opt)][another]+' ')
        if ans == -1 and which_opt == 0:
            ans = 0

        which_opt = random.randint(0, 2)
        print("   (2) " + all_word_list[opt.pop(which_opt)][another]+' ')
        if ans == -1 and which_opt == 0:
            ans = 1

        which_opt = random.randint(0, 1)
        print("   (3) " + all_word_list[opt.pop(which_opt)][another]+' ')
        if ans == -1 and which_opt == 0:
            ans = 2

        which_opt = 0
        print("   (4) " + all_word_list[opt.pop()][another]+'\n')
        if ans == -1 and which_opt == 0:
            ans = 3
        
        feedback = input("   ")
        if int(feedback)-1 == ans:
            t_num = t_num + 1
            print("\n   True")
            jp_listen.speak(driver, all_word_list[num][0], False, 2)
            print("----------------")
        else:
            print("\n   False")
            print("   Ans is " + all_word_list[num][another])
            jp_listen.speak(driver, all_word_list[num][0], False, 2)
            wrong_ans.append(num)
            print("----------------")

    print("Score: " + str(t_num) + '/' + q_num)
    if t_num != int(q_num):
        print("Wrong answer: ")
        for i in range(0, int(q_num)-t_num):
            num = wrong_ans.pop(0)
            print(all_word_list[num][0] + '\t' + all_word_list[num][1])

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
            jp_listen.speak(driver, all_word_list[num][0], False, 2)
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
            
            jp_listen.speak(driver, all_word_list[num][0], False, 2)
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
