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
    in_list = in_data.split('\t');

    cur.execute("INSERT INTO "+sys.argv[1]+"(jp, ch, ks, num, index) Values ('"+in_list[0]+"', '"+in_list[1]+"', '"+in_list[2]+"', '"+in_list[3]+"', '"+in_list[4]+"');")
    


conn.commit()
conn.close()
