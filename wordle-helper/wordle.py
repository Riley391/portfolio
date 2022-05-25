# TODO: add yellow letter (requiredCharacters) functionality with consideration for position
# TODO: create console-based interface for the program

import csv

def buildDictionary():
    dictionary = []
    with open("./wordle-helper/wordle-dictionary.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            dictionary.append(row)
    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i][0].lower()
    return dictionary

def buildTestWordComposition(testWord):
    testWordComposition = []
    for i in range(len(testWord)):
        if testWord[i] == "*":
            testWordComposition.append(i)
    return testWordComposition

def buildThreshold(testWord):
    threshold = 0
    for character in testWord:
        if character != "*":
            threshold += 1
    return threshold

def checkForSoftMatches(dictionary, testWord, threshold):
    resultSet = []
    for word in dictionary:
        testThreshold = 0
        for i in range(5):
            if testWord[i] == "*":
                continue
            elif testWord[i] == word[i]:
                testThreshold += 1
        if testThreshold == threshold:
            resultSet.append(word)
    return resultSet

def checkForDisallowedCharacters(resultSet, disallowedCharacters):
    i = 0
    while i < len(resultSet):
        j = 0
        while j < len(resultSet[i]):
            for character in disallowedCharacters:
                if resultSet[i][j] == character:
                    try:
                        resultSet.remove(resultSet[i])
                    finally:
                        i = 0
                        j -= 1
                        break
            j += 1
        i += 1
    return resultSet

def checkForRequiredCharacters(resultSetNoDisallowedCharacters, requiredCharacters, testWordComposition):
    resultSetChecked = []
    m = 0
    resultSetCheckedLength = 0
    while m < len(resultSetNoDisallowedCharacters):
        for aCharacter in requiredCharacters:
            for number in testWordComposition:
                if resultSetNoDisallowedCharacters[m][number] == aCharacter:
                    resultSetChecked.append(resultSetNoDisallowedCharacters[m])
                    break
                resultSetCheckedLength = len(resultSetChecked)
            if len(resultSetChecked) != resultSetCheckedLength:
                break
        m += 1
    return resultSetChecked

def wordleHelper(testWord, requiredCharacters=[], disallowedCharacters=[]):
    dictionary = buildDictionary()
    testWordComposition = buildTestWordComposition(testWord)
    threshold = buildThreshold(testWord)
    resultSet = checkForSoftMatches(dictionary, testWord, threshold)
    resultSetNoDisallowedCharacters = checkForDisallowedCharacters(resultSet, disallowedCharacters)
    resultSetChecked = checkForRequiredCharacters(resultSetNoDisallowedCharacters, requiredCharacters, testWordComposition)
    if not resultSetChecked:
        return resultSetNoDisallowedCharacters
    return resultSetChecked

def printWordleHelper(testWord, requiredCharacters=[], disallowedCharacters=[]):
    for word in wordleHelper(testWord, requiredCharacters, disallowedCharacters):
        print(word)

printWordleHelper("cro**", [], ['a', 'n', 'e', 'u', 'p'])