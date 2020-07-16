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


def listToString(list):
    str = ""
    for i in list:
        str = str + i + " "
    return str


def TwoDListtoList(list):
    reallist = []
    for i in list:
        for j in i:
            reallist.append(j)
    return reallist


def countWords(list):
    wordList = []
    counter1 = 0
    for i in list:

        wordList.append(WordObject(i))

        for j in wordList:
            if (j.returnWord().lower() == i.lower()):
                # remove
                #list.remove(j)
                # increase
                #wordList[counter1].increase(1)
                #print("yuh")
                j.increase(1)
        counter1 = counter1 + 1


    print("before")
    wordList = noRepeats(wordList)
    print("after")
    for thing in wordList:
        if (thing.returnWord().lower() == "Comtech".lower()):
            print(thing.returnNumber())
    for i in wordList:
        print(i.returnWord() + str(i.returnNumber()))
    return wordList

def noRepeats(list):
    # secondList = []
    # for element in list:
    #     secondList.append(element)
    #
    #
    # for element in list:
    #     count = 0
    #     while count < len(secondList):
    #         if element == secondList[count]:
    #             continue
    #         else:
    #             if element.returnName() == secondList[count].returnName


    for element in list:
        elementPosition = list.index(element) + 1
        while elementPosition < len(list):
            if element.returnWord().lower() == list[elementPosition].returnWord().lower():
                element.increase(list[elementPosition].returnNumber())

                del list[elementPosition]
            elementPosition +=1

    return list









def analyser(analyzerlist):


    counter = 1
    output = codecs.open('Output.txt', "w+", encoding='utf-8')
    # loops through OG List (getting a list of each line)
    for items in OGList():
        listOfWords = []
        # loops through each word in list (each word of a company name)
        for item in items:
            # comapres word to the Ultimate Word List
            for wordObject in analyzerlist:
                # if equal, adds the word object to a list
                if item.lower() == wordObject.returnWord().lower():
                    listOfWords.append(wordObject)

    # variable containing leastFrequentWord
        if len(listOfWords) > 0:
            leastFrequentWord = listOfWords[0]

            # for each word in list of words, compares it to leastfrequentword
            for word in listOfWords:
                if word.returnNumber() < leastFrequentWord.returnNumber():
                    leastFrequentWord = word

            output.write(str(counter) + " " + leastFrequentWord.returnWord()+"\n")
            counter +=1
        else:
            output.write(str(counter) + "Name is empty \n" )
            counter +=1

analyser(countWords((TwoDListtoList(OGList()))))
