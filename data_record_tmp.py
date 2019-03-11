import sys
import psycopg2

conn = psycopg2.connect(database="jp_lr", sslmode='require')

print("connect successful")

cur = conn.cursor()

"""
cur.execute('CREATE TABLE '+sys.argv[1]+'''
        (jp text, -- japanese
         ch text, -- chinese
         ks text, -- kanji
         num int, -- remember number
         index int
         );''')
"""

num = input("How many? ")

for i in range(0, int(num)):
    in_data = input()
    in_list = in_data.split();

    cur.execute("INSERT INTO "+sys.argv[1]+"(num, type, content) Values ('"+in_list[0]+"', '"+in_list[1]+"', '"+in_list[2]+"');")
    


conn.commit()
conn.close()
