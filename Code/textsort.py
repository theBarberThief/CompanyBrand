import codecs
from WordObject import WordObject


def OGList():
    #opens textfile
    f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
    text = f.readlines()
    finalList = []
    for line in text:

        myList = []
        word = ""
        for letter in line:

            #adds letter to the word
            if letter.isalnum():
                word += letter


            #creates a new word if not a letter
            else:
                #only adds words that are more than 1 letter long
                if len(word) > 1:
                    myList.append(word)
                word = ""
        final = ""
        for element in myList:
            final += element + " "

        finalList.append(myList)
    return finalList



def countWords(inputList):

    print(inputList)

    #creates keyvalue dictionary
    words = {}

    for line in inputList:
        for word in line:
            words[word] = words.get(word, 0) + 1
    return words

def analyser():
    words = countWords(OGList())
    count = 1
    output = codecs.open('Output.txt', "w+", encoding='utf-8')


    for line in OGList():

        #makes sure line length is greater than 1
        if len(line) > 0:

            #sets leastcommonword as first word
            leastCommonWord = line[0]
            lowestFrequency = float("inf")
            for word in line:

                #checks if frequency is smaller than lowest frequency in the line
                frequency = words[word]
                if frequency < lowestFrequency:
                    lowestFrequency = frequency
                    leastCommonWord = word
            output.write(str(count) + " " + leastCommonWord + "\n")
            count += 1


analyser()
