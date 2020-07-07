import codecs

f = codecs.open('CompanyEN.txt', "r", encoding='utf-8')
o = codecs.open('Output.txt', "w+", encoding='utf-8')
text = f.readlines()
count = 0
for line in text:
    myList = []
    word = ""
    charCount = 0
    for char in line:
        if char == '.':
            print("WOWOWOW")
        if char != (' ' or '(' or ')' or '.' or ','):
            word += char
            charCount += 1

        # if last letter
        if charCount == len(line) - 1:
            myList.append(word)
        else:
            myList.append(word)
            word = ""
            charCount += 1
    final = ""
    for element in myList:
        final += element

    print(final)
