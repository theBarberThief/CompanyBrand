import codecs
from WordObject import WordObject
import re
import numpy as np

def removeSymbols():
    #opens textfile
    f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
    text = f.readlines()
    finalList = []
    for line in text:
        myList = list(filter(None, re.split(r'[,.();（）；，&\r\n| ]',line)))
        finalList.append(myList)
    return finalList


def countWords(inputList):



    #creates keyvalue dictionary
    words = {}

    for line in inputList:
        for word in line:
            words[word] = words.get(word, 0) + 1
    return words

def analyser():
    removeSymbols_words = removeSymbols()
    words = countWords(removeSymbols_words)
    count = 1
    output = codecs.open('Output.txt', "w+", encoding='utf-8')

    for line in removeSymbols_words:
        # makes sure line length is greater than 1
        if len(line) > 0:
            # sets leastcommonword as first word
            least_common_word = line[0]
            lowest_frequency = float("inf")
            for word in line:
                # checks if frequency is smaller than lowest frequency in the line
                frequency = words[word]
                if frequency < lowest_frequency:
                    lowest_frequency = frequency
                    least_common_word = word
            output.write(str(count) + " " + least_common_word + "\n")
            count += 1


analyser()

