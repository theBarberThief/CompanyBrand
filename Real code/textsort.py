import codecs

f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
o = codecs.open('Output.txt', "w+", encoding='utf-8')
text = f.readlines()
count = 0
for line in text:

    myList = []
    word = ""
    charCount = 0
    spaceCounter = 0
    for letter in line:
        if letter.isalnum():
            word += letter
        else:
            myList.append(word)
            word = ""
    final = ""
    for element in myList:
        final += element

    print(final)
