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

const howManyToTheJackpot = (numberToBeat, charToMatch=undefined) => {
    let defaultChecker = charToMatch === undefined;
    let numberToWin = 0;
    let i = 1;
    while (numberToWin < numberToBeat) {
        let hexCode = getRandomHex(numberToBeat);
        if (defaultChecker) {
            charToMatch = hexCode[0];
        }
        for (let i = 0; i < numberToBeat; i++) {
            if (hexCode[i] == charToMatch) {
                numberToWin++;
            }
        }
        if (numberToWin == numberToBeat) {
            let attempts = i == 1 ? "attempt" : "attempts";
            let formattedI = String(i).replace(/(.)(?=(\d{3})+$)/g,'$1,')
            console.log(`It took ${formattedI} ${attempts} to find this hexadecimal number: ${hexCode}`);
        }
        else {
            numberToWin = 0;
            i++;
        }
    }
}

findTheJackpot(1000, 3);
howManyToTheJackpot(4, "f");