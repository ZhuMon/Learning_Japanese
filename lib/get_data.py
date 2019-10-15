from openpyxl import load_workbook
from openpyxl import Workbook

class Word():
    def __init__(self, jp = None, ch = None, ks = None, n = 0):
        self.jp = jp
        self.ch = ch
        self.ks = ks
        self.n  = n
    def get(self, index):
        """ 
            index: 
                0 -> jp 日文
                1 -> ch 中文
                2 -> ks 漢字
        """
        if index == 0:
            return self.jp
        elif index == 1:
            return self.ch
        elif index == 2:
            return self.ks

class XlwingsData():
    def __init__(self, file_name, sheet, name):
        None

class PyxlData():
    def __init__(self, file_name, sheet):
        wb = load_workbook(file_name)
        #ws = wb.active
        self.ws = wb.get_sheet_by_name(sheet)

        self.lessons = self.getLessons()

    def getLessons(self):
        tmp = []
        for i in range(0, self.ws.max_column):
            column = list(self.ws.columns)[i]
            if column[0].value != None and column[1].value == None:
                tmp.append(column[0].value)
        return tmp
    
    def getNextLesson(self, index):
        for i in range(index+1, self.ws.max_column):
            column = list(self.ws.columns)[i]
            if column[0].value != None and column[1].value == None:
                return i

    def getWords(self, lesson):
        col_lesson = self.lessons.index(lesson) # column number of the lesson
        next_lesson = self.getNextLesson(col_lesson)
        for i in range(0, self.ws.max_row):
            word = Word()
            for j in range(col_lesson+1, next_lesson):
                if list(self.ws.columns)[j][0] == "中文":
                    word.ch = self.ws.cell(row=i, column=j)
                elif list(self.ws.columns)[j][0] == "平假名":
                    word.jp = self.ws.cell(row=i, column=j)



class DataBase():
    def __init__(self, file_name, sheet):
        if 1 == 2:# excel is opened
            # use xlwings
            self.xls = XlwingsData(file_name, sheet)
        else:
            # use pyxl
            self.xls = PyxlData(file_name, sheet)
       

if __name__ == "__main__":
    db = DataBase("../the_word.xlsx", "單字")
