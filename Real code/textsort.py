import codecs
def OGList():
    f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
    o = codecs.open('Output.txt', "w+", encoding='utf-8')
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

        print(final)
        finalList.append(myList)
    return finalList