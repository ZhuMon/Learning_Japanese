import random

word = ["" ,"k","s","t","n","h","m","y","r","w"]
alpha = ["a","i","u","e","o"]
for i in range(0, 5):
    a = random.randint(0,9)
    
    b = random.randint(0,4)
    if a == 2 and b == 1:
	print "shi"
	continue
    elif a == 3 and b == 1:
	print "chi"
	continue
    elif a == 3 and b == 2:
	print "tsu"
	continue
    elif a == 5 and b == 2:
	print "fu"
	continue
    elif a == 7 and (b == 1 or b == 3):
	continue
    elif a == 9 and (b > 0 and b < 4):
	continue
    else:
	print word[a]+alpha[b]

