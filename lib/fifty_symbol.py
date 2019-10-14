import random

class FiftySymbol():
    def __init__(self):
        self.word = ["" ,"k","s","t","n","h","m","y","r","w"]
        self.alpha = ["a","i","u","e","o"]
        self.table = ["あ", "い", "う", "え", "お",
                      "か", "き", "く", "け", "こ",
                      "さ", "し", "す", "せ", "そ",
                      "た", "ち", "つ", "て", "と",
                      "な", "に", "ぬ", "ね", "の",
                      "は", "ひ", "ふ", "へ", "ほ",
                      "ま", "み", "む", "め", "も",
                      "や",   "", "ゆ",   "", "よ",
                      "ら", "り", "る", "れ", "ろ",
                      "わ",   "",   "",   "", "ん"]
        self.state = False

    def start(self):
        try:
            self.state = True
            while self.state:

                a = random.randint(0,9)
                b = random.randint(0,4)
                question = ""
                if a == 2 and b == 1:
                    question = "shi"
                elif a == 3 and b == 1:
                    question = "chi"
                elif a == 3 and b == 2:
                    question = "tsu"
                elif a == 5 and b == 2:
                    question = "fu"
                elif a == 7 and (b == 1 or b == 3):
                    continue
                elif a == 9 and (0 < b < 4):
                    continue
                else:
                    question = self.word[a]+self.alpha[b]
                out = self.table[a*5+b]
                
                out_list = random.sample(self.table, 9)
                out_list = list(filter(lambda a: a != '', out_list))
                if out in out_list:
                    out_list.remove(out)
                out_list = random.sample(out_list, 3)

                yield list([question, out, out_list])
        except KeyboardInterrupt:
            print("Shutting Down")

    def stop(self):
        self.state = False

if __name__ == "__main__":
    func = FiftySymbol()
    func.start()
