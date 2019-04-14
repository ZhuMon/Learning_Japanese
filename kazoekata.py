import random
import psycopg2
import sys

conn = psycopg2.connect(database="jp_lr", sslmode='require')
cur = conn.cursor()

cur.execute("SELECT * FROM obj")
obj_list = cur.fetchall()

cur.execute("SELECT * FROM kazo")
kazo_list = cur.fetchall()


q = input("How many? ")

for i in range(0, int(q)):
    num = random.randint(1, 11)
    n = random.randint(0, len(obj_list)-1)

    if i % 2 == 0:
        num = random.choice([1, 3, 6, 8, 10])

    ans_kazo_list = []
    for kazo in kazo_list:
        if kazo[1] == obj_list[n][1]:
            ans_kazo_list.append(kazo)

    ans_kazo_list.sort()
    
    print(i+1,". ",obj_list[n][0]," ",num)

    ans = input()

    print()
    print("------------")
    if ans == ans_kazo_list[num-1][2]:
        print("True")
    else:
        print("False")
        print("The answer is: " + ans_kazo_list[num-1][2])
    
    print("------------")
    print()

conn.close()

