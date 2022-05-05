import random
import pandas as pd

fileName = 'wordFrequency.xlsx'
df = pd.read_excel(fileName, sheet_name='4 forms (219k)')

df = df.drop(columns=['rank', 'freq', '#texts', '%caps', 'blog', 'web', 'TVM', 'spok', 'fic', 'mag', 'news', 'acad',
                      'blogPM', 'webPM', 'TVMPM', 'spokPM', 'ficPM', 'magPM', 'newsPM', 'acadPM'])

dictionary = df['word'].to_list()


def goAgain():
    answer = input("Would you like to search for another word? (y/n)\n")
    if answer == 'y':
        findThatWord()


def findThatWord():
    wordToFind = input("What word should I search my records for?: ")

    try:
        result = dictionary.index(wordToFind.lower())
        print(f"{wordToFind.title()} is number {result} in my list of the most common words in the English language.")
        goAgain()
    except ValueError:
        print(f"{wordToFind.title()} is not in my records.")
        goAgain()


def caesar(string, keyNumber):
    ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,!?')
    inputList = list(string)

    for j in range(len(inputList)):
        if inputList[j] == ' ' or inputList[j] == "'":
            continue
        index = ALPHABET.index(inputList[j])
        newIndex = index + keyNumber
        if newIndex >= len(ALPHABET):
            newIndex -= len(ALPHABET)
        inputList[j] = ALPHABET[newIndex]

    return ''.join(inputList)


def decrypt(string):
    for j in range(1, 66):
        newList = caesar(string, j).split()
        number_of_real_words = 0
        for word in newList:
            for item in dictionary:
                if type(item) != str:
                    continue
                if len(item) <= 2:
                    continue
                if word.lower() == item:
                    # return ' '.join(newList)
                    # print(' '.join(newList))
                    number_of_real_words += 1
        if number_of_real_words >= 1:
            # return ' '.join(newList)
            print(' '.join(newList))


def getKey():
    tempKey = random.randint(1, 66)
    while tempKey == 26 or tempKey == 66:
        tempKey = random.randint(1, 66)
    return tempKey


key = getKey()
encryptionString = input("Enter your sentence to be encrypted and decrypted here: ")

encryption = caesar(encryptionString, key)

print()
print(encryptionString)
print()
print(caesar(encryptionString, key))
print()
decrypt(encryption)
print()
findThatWord()
