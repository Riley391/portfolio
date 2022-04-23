const getRandomHex = (length) => {
    let result = "";
    for (let i = 0; i < length; i++) {
        let digit = (Math.random() * 16 | 0).toString(16);
        result += digit;
    }
    return result;
}

const findTheJackpot = (numberOfAttempts, numberToBeat, charToMatch=undefined) => {
    let defaultChecker = charToMatch === undefined;
    for (let i = 0; i < numberOfAttempts; i++) {
        let hexCode = getRandomHex(numberToBeat);
        if (defaultChecker) {
            charToMatch = hexCode[0];
        }
        let numberToWin = 0;
        for (let i = 0; i < numberToBeat; i++) {
            if (hexCode[i] == charToMatch) {
                numberToWin++;
            }
        }
        if (numberToWin == numberToBeat) {
            console.log(hexCode);
        }
    }
}

findTheJackpot(1000000000, 10);