import codecs
import numpy as np
import re

def main():

    #number of companies
    company_count = 0

    #2D List of all the company names without symbols
    no_symbol_list = []

    #opens textfile
    f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')


    text = f.readlines()

    words_set = set()

    for line in text:
        
        company_count += 1

        #removes symbol from the line
        new_line = list(filter(None, re.split(r'[,.();（）；，&\r\n| ]',line)))

        #adds the new line to no_symbol_list
        no_symbol_list.append(new_line)

        #adds each word to word set
        for word in new_line:
            words_set.add(word.lower())

    #turns the word set into a list
    result_list = list(words_set)

    #creates a matrix with companycount rows, and result list coloumns
    bow = np.zeros((company_count, len(result_list)))

    changeAll(company_count, no_symbol_list, result_list, bow)
    columnnAdding(company_count, no_symbol_list, result_list, bow)





def getLine(line_number, my_noSymbolList):
    
    line = my_noSymbolList[line_number]
    return line




def changeOneLine(input_list, lineNumber, my_resultList, bow_matrix):
    for word in input_list:
        position = my_resultList.index(word.lower())
        bow_matrix[lineNumber][position]+=1


def changeAll(my_companyCount, my_noSymbolList, my_resultList, bow_matrix):
    count = 0


    while count < my_companyCount:
        line = getLine(count, my_noSymbolList)
        changeOneLine(line, count, my_resultList, bow_matrix)
        count += 1
   


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