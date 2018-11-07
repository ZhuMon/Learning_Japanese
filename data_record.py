import sys

kind = input("Which kind of data? (單字(w) 慣用語(p)) ")
num  = input("How many? ")

if kind is 'w':
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'a')
    else:
        file = open('words', 'a')
    
    print("日文\t中文")

    for i in range(0, int(num)):
        in_data = input()
        file.write(in_data+'\n')

elif kind is 'p':
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'a')
    else:
        file = open('phrases', 'a')

    print("片語（無漢字） 中文 片語（有漢字）")

    for i in range(0, int(num)):
        in_data = input()
        file.write(in_data+'\n')
