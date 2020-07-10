import codecs
import nltk
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

        print(final)
        finalList.append(myList)
    return finalList

def listToString(list):
    str = ""
    for i in list:
        str = str + i + " "
    return str

#shit
def returnNouns(str):
    Nouns = []
    sentence = nltk.word_tokenize(str)
    tagged = nltk.pos_tag(sentence)
    print(tagged)
    for word,pos in tagged:

        if (pos == 'NNP' or pos == 'NNPS' ):
            Nouns.append(word)

    print(listToString(Nouns))
    return Nouns


#def wordNumbers (List)
returnNouns("Jackson went to China on a rainy day!")

