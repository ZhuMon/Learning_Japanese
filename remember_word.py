import random
import jp_listen
import ReuseChrome
import sys
import json
import psycopg2

conn = psycopg2.connect(database="jp_lr", sslmode='require')
cur = conn.cursor()

word_key = ['jp', 'ch', 'ks', 'n']

"""
if len(sys.argv) == 2:
    infile = open(sys.argv[1], 'r')
else:
    infile = open('test', 'r')
    #infile = open('words', 'r')
"""
"""
word_list = []
line_list = []
all_word_list = []
"""
if len(sys.argv) < 2:
    table_name = input("Please enter the table name ")
    cur.execute("SELECT * from "+table_name)
else:
    cur.execute("SELECT * from "+sys.argv[1])

all_word_list = cur.fetchall()

"""
file_data = infile.readline()
while file_data :
    json_data = json.loads(file_data)
    all_word_list.append(json_data)
    file_data = infile.readline()

"""
"""
content = infile.read()
line_list = content.splitlines(False)

for i in range(0, len(line_list)):
    #word_list = line_list[i].split('\t')
    
    all_word_list.append(word_list) 
"""

mode = input("Which mode? (選擇題(a) 問答題(b)) ")
q_num = input("How many questions? ") # question number
#jp_or_ks = input("which description? (平假名or片假名(jp) 有漢字(ks)) ")

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
        while all_word_list[num][3] >= 5:
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

        ch_or_jp = random.randint(0, 2)
        another  = 0 if ch_or_jp>0 else 1

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
            print("----------------")
        else:
            print("\n   False")
            print("   Ans is " + all_word_list[num][another])
            wrong_ans.append(num)
            print("----------------")

        if ord(all_word_list[num][2][0]) > 128:#if ks isn't english
            jp_listen.speak(driver, all_word_list[num][2], False, 2)
        else:
            jp_listen.speak(driver, all_word_list[num][0], False, 2)

    print("Score: " + str(t_num) + '/' + q_num)
    if t_num != int(q_num):
        print("Wrong answer: ")
        for i in range(0, int(q_num)-t_num):
            num = wrong_ans.pop(0)
            out1 = all_word_list[num][0]
            if len(out1) > 3:
                out1 = out1 + '\t'
            else:
                out1 = out1 + '\t\t'
            out2 = all_word_list[num][2]
            if len(out2) > 3:
                out2 = out2 + '\t'
            else:
                out2 = out2 + '\t\t'
            print(out1 + out2 + all_word_list[num][1])

elif mode is 'b':
    wk_mode = input("Write or key in? (write(w) key in(k)) ")
    if wk_mode is 'w':
        for i in range(0, int(q_num)-1 ):
            num = random.randint(0, len(all_word_list)-1)
            while all_word_list[num][3] > 4:
                num = random.randint(0, len(all_word_list)-1)
            ch_or_jp = random.randint(0, 2)
            another  = 0 if ch_or_jp>0 else 1
            
            print(str(i+1) + ". " + all_word_list[num][ch_or_jp])
            input()
            print(all_word_list[num][0])
            print(all_word_list[num][2] +'\t' +all_word_list[num][1])

            if ord(all_word_list[num][2][0]) > 128:#if ks isn't english
                jp_listen.speak(driver, all_word_list[num][2], False, 2)
            else:
                jp_listen.speak(driver, all_word_list[num][0], False, 2)
            print("----------------")

    elif wk_mode is 'k':
        t_num = 0
        wrong_ans = []
        for i in range(0, int(q_num) ):
            num = random.randint(0, len(all_word_list)-1)
            
            # check whether all word have bean learned
            larger_treshold_flag = 0
            for word in all_word_list:
                if word[3] <= 4:
                    larger_treshold_flag = 1

            if larger_treshold_flag == 0:
                q_num = str(i)
                break

            while all_word_list[num][3] > 4:
                num = random.randint(0, len(all_word_list)-1)

            ch_or_jp = random.randint(1, 2)

            if ch_or_jp == 2 and all_word_list[num][0] == all_word_list[num][2]:
                ch_or_jp = 1

            if ch_or_jp == 1:
                print(str(i+1) + ". " + all_word_list[num][1])
                feedback = input("   日文： ")
                if feedback == all_word_list[num][0] or feedback == all_word_list[num][2]:
                    print("\n   True")
                    t_num = t_num + 1
                    all_word_list[num][3] = all_word_list[num][3] + 1
                    cur.execute("UPDATE "+sys.argv[1]+" set num = num + 1 where jp='" + all_word_list[num][0]+"'")
                    conn.commit()
                else:
                    print("\n   False")
                    wrong_ans.append(num)
                    print("   Ans : " + all_word_list[num][0])
                    #cur.execute("UPDATE "+sys.argv[1]+" set num = num - 1 where jp='" + all_word_list[num][0]+"'")
                    #conn.commit()
                    

            elif ch_or_jp == 2:
                print(str(i+1) + ". " + all_word_list[num][2])

                if ord(all_word_list[num][2][0]) < 128:
                    feedback = input("   片假名： ")
                else:
                    feedback = input("   平假名： ")
                if feedback == all_word_list[num][0]:
                    print("\n   True")
                    t_num = t_num + 1
                    all_word_list[num][3] = all_word_list[num][3] + 1
                    cur.execute("UPDATE "+sys.argv[1]+" set num = num + 1 where jp='" + all_word_list[num][0]+"'")
                    conn.commit()
                else:
                    print("\n   False")
                    wrong_ans.append(num)
                    print("   Ans : " + all_word_list[num][0])
                    print("         " + all_word_list[num][2])
                    #cur.execute("UPDATE "+sys.argv[1]+" set num = num - 1 where jp='" + all_word_list[num][0]+"'")
                    conn.commit()
            
            if ord(all_word_list[num][2][0]) > 128:#if ks isn't english
                jp_listen.speak(driver, all_word_list[num][2], False, 2)
            else:
                jp_listen.speak(driver, all_word_list[num][0], False, 2)
            print("----------------")

        if int(q_num) == 0:
            print("Already learn everything.")
            print("Improve treshold or change database.")
        else:
            print("Score: " + str(t_num) + '/' + q_num)

        if t_num != int(q_num):
            print("Wrong answer: ")
            for i in range(0, int(q_num)-t_num):
                num = wrong_ans.pop(0)
                
                out1 = all_word_list[num][0]
                if len(out1) > 3:
                    out1 = out1 + '\t'
                else:
                    out1 = out1 + '\t\t'
                out2 = all_word_list[num][2]
                if len(out2) > 3:
                    out2 = out2 + '\t'
                else:
                    out2 = out2 + '\t\t'
                print(out1 + out2 + all_word_list[num][1])
            

cont_web = input("Do you continue to learn? Yes(y)/No(n) ")
web_id_w = open('id', 'w')
if cont_web is 'y':
    web_id_w.write(driver.command_executor._url+'\n')
    web_id_w.write(driver.session_id + '\n')
    web_id_w.close()
    #del driver
else:
    driver.quit()
 

conn.close()
