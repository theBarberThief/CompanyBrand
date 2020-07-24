import codecs
import numpy as np
import re

def main():
    companyCount = 0
    noSymbolList = []

    f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
    text = f.readlines()

    wordsset = set()

    for line in text:
        
        companyCount += 1
        newLine = list(filter(None, re.split(r'[,.();（）；，&\r\n| ]',line)))

       
        noSymbolList.append(newLine)

        for word in newLine:
            wordsset.add(word.lower())

    resultList = list(wordsset)
    bow = np.zeros((companyCount, len(resultList)))

    changeAll(companyCount, noSymbolList, resultList, bow)
    columnnAdding(companyCount, noSymbolList, resultList, bow)





def getLine(lineNumber, my_noSymbolList):
    
    line = my_noSymbolList[lineNumber]
    return line




def changeOneLine(input_list, lineNumber, my_resultList, bow_matrix):
    for word in input_list:
        position = my_resultList.index(word.lower())
        bow_matrix[lineNumber][position]+=1


def changeAll(my_companyCount, my_noSymbolList, my_resultList, bow_matrix):
    count = 0
    print("before")

    while count < my_companyCount:
        line = getLine(count, my_noSymbolList)
        changeOneLine(line, count, my_resultList, bow_matrix)
        count += 1
    print("after")


def columnnAdding(companyCount, my_noSymbolList, my_resultList, my_bow):
    sumList = my_bow.sum(axis = 0).tolist()
    output = codecs.open('Output.txt', "w+", encoding='utf-8')
   

    count = 1
    for line in my_noSymbolList:
        # makes sure line length is greater than 1
        if len(line) > 0:
            # sets leastcommonword as first word
            least_common_word = line[0]
            lowest_frequency = float("inf")
            for word in line:
                # checks if frequency is smaller than lowest frequency in the line
               
                word_index = my_resultList.index(word.lower())
                frequency = sumList[word_index]
                if frequency < lowest_frequency:
                    lowest_frequency = frequency
                    least_common_word = word
            output.write(str(count) + " " + least_common_word + "\n")
            count += 1 




main()
print("finish")