import sys
import json

kind = input("Which kind of data? (單字(w) 慣用語(p)) ")
num  = input("How many? ")

if kind is 'w':
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'a')
    else:
        file = open('json_words', 'a')
    
    print("日文\t中文\t漢字")

    for i in range(0, int(num)):
        in_data = input()
        in_list = in_data.split();
        mydict = {}
        mydict['jp'] = in_list[0]
        mydict['ch'] = in_list[1]
        mydict['ks'] = in_list[2]
        myjson = json.dumps(mydict)
        file.write(myjson)
        file.write('\n')

elif kind is 'p':
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'a')
    else:
        file = open('json_phrases', 'a')

    print("片語（無漢字） 中文 有無漢字 片語（有漢字）有無對應句 對應句 對應句有無漢字 對應句（有漢字）")

    for i in range(0, int(num)):
        in_data = input()
        in_list = in_data.split();
        mydict = {}
        mydict['jp'] = in_list[0]
        mydict['ch'] = in_list[1]
        mydict['ks_bool'] = in_list[2]
        mydict['ks'] = in_list[3]
        mydict['aw_bool'] = in_list[4]
        mydict['aw_jp'] = in_list[5]
        mydict['aw_ks_bool'] = in_list[6]
        mydict['aw_ks'] = in_list[7]
        myjson = json.dumps(mydict)
        file.write(myjson)
        file.write('\n')
