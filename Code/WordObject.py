class WordObject:
    number = 0
    word = ""

    def __init__(self, word):
        self.word = word

    def increase(self, num):
        self.number = self.number + num

    def returnNumber(self):
        return self.number

    def returnWord(self):
        return self.word

    def changeNumber(self, num):
        self.number = num

    def setName(self, string):
        self.word = string
