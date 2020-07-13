import codecs


def OGList():
    f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
    o = codecs.open('Output.txt', "w+")

    text = f.readlines()
    finalList = []
    for line in text:

        myList = []
        word = ""
        for letter in line:
            if letter.isalnum():
                word += letter
            else:
                myList.append(word)
                word = ""
        final = ""
        for element in myList:
            final += element + " "

        o.write(final)
        finalList.append(myList)

    print(finalList)
    return finalList


def listToString(list):
    str = ""
    for i in list:
        str = str + i + " "
    return str

def analyser(list):
    listOfWords = []
    #loops through OG List (getting a list of each line)
    for items in OGList():
        #loops through each word in list (each word of a company name)
        for item in items:
            #comapres word to the Ultimate Word List
            for wordObject in list:
                #if equal, adds the word object to a list
                if item == wordObject.returnWord():
                    listOfWords.append(wordObject)

   #variable containing leastFrequentWord
    leastFrequentWord = listOfWords[0]

    #for each word in list of words, compares it to leastfrequentword
    for word in listOfWords:
        if word.returnNumber() < leastFrequentWord.returnNumber():
            leastFrequentWord = word

    return leastFrequentWord
OGList()
