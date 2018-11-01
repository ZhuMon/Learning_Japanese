kind = input("Which kind of data? (單字(w) 慣用語(p)) ")
num  = input("How many? ")

if kind is 'w':
    file = open('words', 'a')
    
    print("日文\t中文")

    for i in range(0, int(num)):
        in_data = input()
        file.write(in_data+'\n')

elif kind is 'p':
    file = open('phrase', 'a')


