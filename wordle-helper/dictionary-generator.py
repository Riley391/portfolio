import csv

filePath = "./wordle-helper/dictionaries/"
fileType = ".csv"
dictionary = []

dictionaryLetterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dictionaryPathList = []

for letter in dictionaryLetterList:
    dictionaryPathList.append(filePath + letter + fileType)

for path in dictionaryPathList:
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in spamreader:
            dictionary.append(row)

for word in dictionary:
    if len(word) == 0:
        dictionary.remove(word)

for i in range(len(dictionary)):
    dictionary[i] = dictionary[i][0]

for i in range(len(dictionary)):
    if dictionary[i][0] == '"':
        mytable = dictionary[i].maketrans('', '', '"')
        dictionary[i] = dictionary[i].translate(mytable)

for i in range(len(dictionary)):
    result = ''
    for character in dictionary[i]:
        if character != ' ':
            result += character
        elif character == ' ':
            break
    dictionary[i] = result

for i in range(len(dictionary)):
    if i + 1 >= len(dictionary):
        continue
    while dictionary[i] == dictionary[i + 1]:
        dictionary.pop(i + 1)

for i in range(len(dictionary)):
    while i < len(dictionary) and len(dictionary[i]) != 5 :
        dictionary.pop(i)

with open('dictionary.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(dictionary)

print("Done!")