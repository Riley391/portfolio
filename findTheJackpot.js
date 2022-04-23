const getRandomHex = (length) => {
    let result = "";
    for (let i = 0; i < length; i++) {
        let digit = (Math.random() * 16 | 0).toString(16);
        result += digit;
    }
    return result;
}

const findTheJackpot = (numberOfAttempts, numberToBeat) => {
    for (let i = 0; i < numberOfAttempts; i++) {
        let hexCode = getRandomHex(numberToBeat);
        let charToMatch = hexCode[0];
        let numberToWin = 1;
        for (let i = 1; i < 6; i++) {
            if (hexCode[i] == charToMatch) {
                numberToWin++;
            }
        }
        if (numberToWin == numberToBeat) {
            console.log(hexCode);
        }
    }
}

findTheJackpot(1000, 3)