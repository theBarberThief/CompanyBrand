class WordObject:
    number = 0
    word = ""

    def __init__(self, word):
        self.word = word

    def increase(self, num):
        WordObject.number = WordObject.number + num

    def returnNumber(self):
        return WordObject.number

    def returnWord(self):
        return WordObject.word
