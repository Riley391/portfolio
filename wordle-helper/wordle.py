# TODO: add disallowedCharacters functionality (work out the bugs)

import csv
dictionary = []

with open("./wordle-helper/dictionary.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            dictionary.append(row)

dictionary = dictionary[0]

for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].lower()

def WordleHelper(testWord):
    testSet = ["album", "alloy", "algae", "alley", "glass"]
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
    """ k = 0
    while k < len(resultSet):
        for letter in resultSet[k]:
            for character in disallowedCharacters:
                if letter == character:
                    resultSet.remove(resultSet[k])
                    k -= 1
        k += 1 """
    return resultSet

print(WordleHelper("all**"))