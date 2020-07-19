import codecs
from WordObject import WordObject


def OGList():
    f = codecs.open('companysamefont.txt', "r", encoding='utf-8')
    text = f.readlines()
    finalList = []
    for line in text:

        myList = []
        word = ""
        for letter in line:
            if letter.isalnum():
                word += letter
            else:
                if len(word) > 1:
                    myList.append(word)
                word = ""
        final = ""
        for element in myList:
            final += element + " "

        finalList.append(myList)
    return finalList



def countWords(botJerry):

    print(botJerry)
    words = {}

    for line in botJerry:
        for word in line:
            words[word] = words.get(word, 0) + 1
    return words

def analyser():
    words = countWords(OGList())
    count = 1
    output = codecs.open('Output.txt', "w+", encoding='utf-8')
    for line in OGList():
        if len(line) > 0:
            leastCommonWord = line[0]
            lowestFrequency = float("inf")
            for word in line:
                frequency = words[word]
                if frequency < lowestFrequency:
                    lowestFrequency = frequency
                    leastCommonWord = word
            output.write(str(count) + " " + leastCommonWord + "\n")
            count += 1


analyser()
