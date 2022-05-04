def caesar(string, keyNumber):
    ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    inputList = list(string)
    for i in range(len(inputList)):
        if inputList[i] == ' ' \
                or inputList[i] == '.' \
                or inputList[i] == ',' \
                or inputList[i] == '!' \
                or inputList[i] == '?':
            continue
        index = ALPHABET.index(inputList[i])
        newIndex = index + keyNumber
        if newIndex >= len(ALPHABET):
            newIndex -= len(ALPHABET)
        inputList[i] = ALPHABET[newIndex]

    return ''.join(inputList)


def decrypt(string):
    for i in range(1, 52):
        newString = caesar(string, i)
        newString = newString.translate({ord(i): None for i in '.,!?'})
        newList = newString.split()
        for j in range(len(newList)):
            newList[j] = newList[j].lower()
        for word in newList:
            if word == 'the':
                return ' '.join(newList)


print(caesar("Hello world, my name is Payton Lommers. I have sensitive information that needs to be seen by the "
             "highest authority immediately!", 15))
encryption = caesar("Hello world, my name is Payton Lommers. I have sensitive information that needs to be seen by the "
                    "highest authority immediately!", 15)

print(decrypt(encryption))
