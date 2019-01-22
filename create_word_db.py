import sys
import psycopg2

conn = psycopg2.connect(database="jp_lr", sslmode='require')

print("connect successful")

cur = conn.cursor()

cur.execute('CREATE TABLE '+sys.argv[1]+'''
        (jp text, -- japanese
         ch text, -- chinese
         ks text, -- kanji
         num int, -- remember number
         index int
         );''')

conn.commit()
conn.close()
