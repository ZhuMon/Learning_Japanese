infile = open('words', 'r')

word_list = []
line_list = []

content = infile.read()
line_list = content.splitlines(False)

for i in range(0, len(line_list)):
    word_list = line_list[i].split('\t')
    print(word_list)
