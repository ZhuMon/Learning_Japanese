import sys
import psycopg2

conn = psycopg2.connect(database="jp_lr", sslmode='require')

cur = conn.cursor()

if len(sys.argv) < 2:
    table = input("Enter the table name: ")
else:
    table = sys.argv[1]

num = input("How many? ")
print("num  index")

for i in range(0, int(num)):
    in_data = input()
    in_list = in_data.split()

    cur.execute('UPDATE '+table+' SET num = '+in_list[0]+' WHERE index = '+in_list[1]+' ;')


conn.commit()
conn.close()
