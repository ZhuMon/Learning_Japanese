import random

#num = random.randint(1, 100000)
num = 11245
out = ""
std = ["", "いち", "に", "さん", "よん", "ご", "ろく", "なな", "はち", "きゅう", "じゅう"]
abn = ["", "", "", "", "し", "", "ろっ", "しち", "はっ", "く"]

print(num)

if num == 100000:
    out = "じゅうまん"
elif (int)(num / 10000) > 0:
    w = (int) (num / 10000)
    out = std[w] + "まん"
    
if num % 10000 / 1000 >= 1:
    k = (int) ((num % 10000 )/ 1000)
    if k != 1 and k != 3 and k != 8:
        out = out + std[k] + "せん"
    elif k == 3:
        out = out + std[3] + "ぜん"
    elif k == 8:
        out = out + abn[8] + "せん"
    elif k == 1:
        out = out + "せん"

if num % 1000 / 100 >= 1:
    h = (int) ((num % 1000) / 100)
    if h != 1 and h != 3 and h != 6 and h != 8:
        out = out + std[h] + "ひゃく"
    elif h == 1:
        out = out + "ひゃく"
    elif h == 3 :
        out = out + abn[h] + "びゃく"
    elif h == 6 or h == 8:
        out = out + abn[h] + "ぴゃく"

if num % 100 / 10 >= 1:
    t = (int) ((num % 100) / 10)
    if t != 1:
        out = out + std[t]

    out = out + std[10]

if num % 10 > 0:
    out = out + std[(int) (num % 10)]

print(out)
