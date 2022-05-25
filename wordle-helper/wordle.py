# TODO: add disallowedCharacters functionality (work out the bugs)

import csv
dictionary = []

with open("./wordle-helper/wordle-dictionary.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            dictionary.append(row)

for i in range(len(dictionary)):
    dictionary[i] = dictionary[i][0]

for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].lower()

""" for i in range(20):
    print(dictionary[i]) """

def WordleHelper(testWord, disallowedCharacters=[]):
    # testSet = ["album", "alloy", "algae", "alley", "glass"]
    resultSet = []
    threshold = 0
    for character in testWord:
        if character != "*":
            threshold += 1
    for word in dictionary:
        testThreshold = 0
        for i in range(5):
            if testWord[i] == "*":
                continue
            elif testWord[i] == word[i]:
                testThreshold += 1
        if testThreshold == threshold:
            resultSet.append(word)
    for dude in resultSet:
        for letter in dude:
            for character in disallowedCharacters:
                if letter == character:
                    resultSet.remove(dude)
    return resultSet

def PrintWordleHelper(testWord, disallowedCharacters=[]):
    for word in WordleHelper(testWord, disallowedCharacters):
        print(word)

PrintWordleHelper("*las*", ['b', 'k'])