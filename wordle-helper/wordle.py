# TODO: add yellow letter (requiredCharacters) functionality with consideration for position in the form of *ab**

import csv
import os
import sys

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
        while resultSet and j < len(resultSet[i]):
            for character in disallowedCharacters:
                if resultSet[i][j] == character:
                    try:
                        resultSet.remove(resultSet[i])
                    finally:
                        i = 0
                        j = -1
                        break
            j += 1
        i += 1
    return resultSet

def checkForRequiredCharacters(resultSetNoDisallowedCharacters, requiredCharacters, testWordComposition):
    resultSetChecked = []
    threshold = len(requiredCharacters)
    m = 0
    resultSetCheckedLength = 0
    while m < len(resultSetNoDisallowedCharacters):
        compareToThreshold = 0
        for aCharacter in requiredCharacters:
            for number in testWordComposition:
                if resultSetNoDisallowedCharacters[m][number] == aCharacter:
                    compareToThreshold += 1
                    break
            if len(resultSetChecked) != resultSetCheckedLength:
                break
        if compareToThreshold == threshold:
            resultSetChecked.append(resultSetNoDisallowedCharacters[m])
            resultSetCheckedLength = len(resultSetChecked)
        m += 1
    return resultSetChecked

def checkTwice(testWord, requiredCharacters, disallowedCharacters):
    disallowedCharacters = checkAgainstDisallowedCharacters(requiredCharacters, disallowedCharacters)
    disallowedCharacters = checkAgainstDisallowedCharacters(testWord, disallowedCharacters)
    return disallowedCharacters

def checkAgainstDisallowedCharacters(checkAgainst, disallowedCharacters):
    disallowedCharactersChecked = disallowedCharacters
    for letter in checkAgainst:
        for character in disallowedCharacters:
            if letter == character:
                disallowedCharactersChecked.remove(character)
    return disallowedCharactersChecked

def wordleHelper(testWord, requiredCharacters=[], disallowedCharacters=[]):
    disallowedCharacters = checkTwice(testWord, requiredCharacters, disallowedCharacters)
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
    print("All possible words are listed below\n\n-----------------------------------------------\n")
    for word in wordleHelper(testWord, requiredCharacters, disallowedCharacters):
        print(word)

def handlePersistentCharacters(disallowedCharactersComplete):
    willDisallowedCharactersPersist = input("Would you like to continue using your previous list of grey letters? (y/n): ")
    if willDisallowedCharactersPersist == "y":
        return disallowedCharactersComplete
    elif willDisallowedCharactersPersist == "n":
        return []
    else:
        print("Please enter a valid character")
        handlePersistentCharacters(disallowedCharactersComplete)

def clearConsole():
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

def buildParsed(unparsed):
    parsed = []
    for letter in unparsed:
        parsed.append(letter)
    return parsed

def handleUserContinue(disallowedCharactersComplete):
    willUserContinue = input("Would you like to use World Helper (tm) again? (y/n): ")
    if willUserContinue == "n":
        sys.exit()
    persistentDisallowedCharacters = handlePersistentCharacters(disallowedCharactersComplete)
    if willUserContinue == "y":
        promptUser(persistentDisallowedCharacters)

def promptUser(persistentDisallowedCharacters=[]):
    clearConsole()
    testWord = input("Please enter your Wordle guess in the form of *la*t where 'l', 'a', and 't' are the green letters from your guess, and the '*'s are yellow or grey letters from your guess: ")
    requiredCharacters = input("Please enter your letters in yellow here in the form of 'abcxyz' (do not enter letters which are already in your Wordle guess string): ")
    disallowedCharacters = input("Please enter your letters in grey here (in the form of 'abcxyz'): ")
    requiredCharactersParsed = buildParsed(requiredCharacters)
    disallowedCharactersParsed = buildParsed(disallowedCharacters)
    disallowedCharactersComplete = persistentDisallowedCharacters + disallowedCharactersParsed
    printWordleHelper(testWord, requiredCharactersParsed, disallowedCharactersComplete)
    handleUserContinue(disallowedCharactersComplete)

promptUser()