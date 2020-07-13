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
    for i in list:
        wordList.append(WordObject(i))


        for j in list:
            if(j.lower() == i.lower()):
                #remove
                list.remove(j)
                #increase
                wordList[counter1].increase(1);
                print("yuh")
        counter1 = counter1 + 1

    for i in wordList:
        print(i.returnWord() + str(i.returnNumber()))
    return wordList
countWords(TwoDListtoList(OGList()))
#a = WordObject("ayay")
#print(a.returnWord())
#print(TwoDListtoList(OGList()))












#def wordNumbers (List)

