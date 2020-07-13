import codecs
from WordObject import WordObject
def OGList():
    f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
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
        for j in i :
            reallist.append(j)
    return reallist
def countWords(list):
    wordList = []
    counter1 = 0
    for i in list:    #goes through list of words(str)
        wordList.append(WordObject(i)) #add a wordobject of the str in wordlist
        for j in list: #goes through the list and removes duplicate, counting in wordobject
            if(j.lower() == i.lower()):

                list.remove(j)
                wordList[counter1].increase(1);
                print("yuh")
        counter1 = counter1 + 1

    for i in wordList: #prints wordlist
        print(i.returnWord() + str(i.returnNumber()))
    return wordList
countWords(TwoDListtoList(OGList())) #gets OGlist converts to 1D list, run countwords
#a = WordObject("ayay")
#print(a.returnWord())
#print(TwoDListtoList(OGList()))












#def wordNumbers (List)

