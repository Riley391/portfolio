# import statements -- random for encryption key generation and pandas for dataframe/excel sheet manipulation
import random
import pandas as pd

# declare constant containing all symbols used in the cipher
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,!?')

# create variable df containing a dataframe based on the excel sheet
fileName = 'wordFrequency.xlsx'
df = pd.read_excel(fileName, sheet_name='4 forms (219k)')

# drop unneeded columns
df = df.drop(columns=['rank', 'freq', '#texts', '%caps', 'blog', 'web', 'TVM', 'spok', 'fic', 'mag', 'news', 'acad',
                      'blogPM', 'webPM', 'TVMPM', 'spokPM', 'ficPM', 'magPM', 'newsPM', 'acadPM'])

# create list of words from df
dictionary = df['word'].to_list()

# function to repeat the findThatWord function based on user input
# TODO: generalize this function with parameters 'message' and 'function'
def goAgain():
    # ask user if they want to run the function again
    answer = input("Would you like to search for another word? (y/n)\n")
    # if so, run the function again
    if answer == 'y':
        findThatWord()
    # if not, terminate the program
    else:
        exit(0)

# function to either find a word by its index number or find an index number based on the word
def findThatWord():
    # ask the user what word or index number the program should search for
    wordToFind = input("What word or index number should I search my records for?: ")
    # newline
    print()
    # try except statement to return a string when the program does not find the word or index number
    try:
        # try except statement to check if user input is of type int or string
        try:
            # if input is int, find the word by index
            wordToFind = int(wordToFind)
            # checks whether wordToFind is outside the bound of dictionary
            if (wordToFind - 1 >= len(dictionary)):
                print(f"{wordToFind} exceeds the bounds of my list of common words in the English language.")
                goAgain()
            else:
                result = dictionary[wordToFind - 1]
                print("\"" + f"{result.title()}" + "\"" + f" is located at number {wordToFind} in my list of most common words in the English language.")
        except ValueError:
            # if input is not int, find the index of the word
            result = dictionary.index(wordToFind.lower())
            print(f"{wordToFind.title()} is number {result} in my list of the most common words in the English language.")
        goAgain()
    except ValueError:
        # if the word or index cannot be found, print this message:
        print(f"{wordToFind.title()} is not in my records.")
        goAgain()

# function to encrypt a string using the caesar cipher (message and encryption key must be passed)
def caesar(string, keyNumber):
    # convert user input string to list
    inputList = list(string)

    # for each character in input string, change it to a different character based on the key
    for j in range(len(inputList)):
        # skip ' ' and "'" (don't change them)
        if inputList[j] == ' ' or inputList[j] == "'":
            continue
        # store character index in variable
        index = ALPHABET.index(inputList[j])
        # calculate and store the new index in a variable
        newIndex = index + keyNumber
        # make sure the new index does not exceed the length of ALPHABET
        if newIndex >= len(ALPHABET):
            newIndex -= len(ALPHABET)
        # change the character to the character at the new index in ALPHABET
        inputList[j] = ALPHABET[newIndex]

    # return the modified list as a string
    return ''.join(inputList)

# decrypt an encrypted string by looping through all possible caesar ciphers
# and finding the ciphers which contain words matching words from the dictionary list
def decrypt(string):
    # declare array to store our successful strings
    result = []
    # loop through every possible caesar cipher
    for j in range(1, 66):
        # generate the caesar cipher for this iteration
        newList = caesar(string, j).split()
        # declare variable to track the number of matched words
        number_of_real_words = 0
        # loop through each word in the generated caesar cipher
        for word in newList:
            # loop through each word in dictionary
            for item in dictionary:
                # skip anything in dictionary that isn't a string
                if type(item) != str:
                    continue
                # skip any words of two letters or shorter (lots of false positives for these words)
                if len(item) <= 2:
                    continue
                # check if the word from the cipher matches the word in the dictionary
                if word.lower() == item:
                    # if so, add 1 to the number of matches
                    number_of_real_words += 1
        # defines the threshold number_of_real_words must reach to be returned in the function
        if number_of_real_words >= 1:
            result.append(' '.join(newList))
            return result

# get a random caesar cipher key
def getKey():
    # sets key to random number between 1 and 66
    tempKey = random.randint(1, 65)
    # does not allow key 26, as the cipher produced is readable in some circumstances
    while tempKey == 26:
        tempKey = random.randint(1, 65)
    return tempKey

# example usage of all functions
key = getKey()
encryptionString = input("Enter your sentence to be encrypted and decrypted here: ")

encryption = caesar(encryptionString, key)

print()
print(encryptionString)
print()
print(caesar(encryptionString, key))
print()
decryption = decrypt(encryption)
for i in range(len(decryption)):
    print(decrypt(encryption)[i])
print()
findThatWord()
