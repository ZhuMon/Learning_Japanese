import random


class MyTime():
    def __init__(self):
        self.hour_l = ["いち", "に", "さん" , "よ" , "ご" , "ろく" , "しち" , "はち", "く" , "じゅう" , "じゅういち" , "じゅうに"]
        self.minute_l = [ "いっ", "に", "さん", "よん", "ご", "ろっ", "なな", "はっ", "きゅう", "じゅっ"]
        self.state = False

    def start(self):
        """ Start function """
        try:
            self.state = True
            while self.state:
                hour = random.randint(1, 12)
                minute = random.randint(0, 59)

                print(str(hour)+":"+str(minute))
                input()

                out = ""
                tmp = int(minute/10)
                if tmp > 1:
                    out = self.minute_l[tmp-1]
                if tmp >= 1 and minute%10 != 0:
                    out = out + self.hour_l[9]
                
                tmp = minute%10
                if tmp == 2 or tmp == 5 or tmp == 7 or tmp == 9:
                    out = out + self.minute_l[tmp - 1] + " ふん"
                else:
                    if tmp != 0 :#and int(minute/10) > 1:
                        out = out + self.minute_l[tmp - 1] + " ぷん"
                    elif tmp == 0:
                        out = out + self.minute_l[9] + " ぷん"
                        
                print(self.hour_l[hour-1] + " じ " + out)

        except KeyboardInterrupt:
            self.state = False
            print("Shutting Down")

    def stop(self):
        self.state = False

if __name__ == "__main__":
    func = MyTime()
    func.start()
