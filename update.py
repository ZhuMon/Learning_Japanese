import sys
import psycopg2

conn = psycopg2.connect(database="jp_lr", sslmode='require')

cur = conn.cursor()

if len(sys.argv) < 2:
    table = input("Enter the table name: ")
else:
    table = sys.argv[1]

cur.execute('SELECT column_name, data_type from information_schema.columns where table_name = \''+table+'\';');
#print(cur.fetchall())
col = []
types = []
for data in cur.fetchall():
    if data[0] != "index":
        col.append(data[0])
        types.append(data[1])

#print(types)
num = input("How many? ")
print("Set what? ", col) 
s = input()

while s not in col:
    if s in col:
        break
    else:
        print("Please input the following")
        print(col)
        s = input()

print("index ", s)
for i in range(0, int(num)):
    in_data = input()
    in_list = in_data.split()

    for j in range(0, len(col)):
        if s == col[j] and types[j] == 'text':
            in_list[1] = "\'"+in_list[1]+"\'"

    cur.execute('UPDATE '+table+' SET '+s+' = '+in_list[1]+' WHERE index = '+in_list[0]+' ;')


conn.commit()
conn.close()
