// I'm tired of getting confused between Python and JS so I imported my own print() function
const { print } = require('./module');

// Generates a hex-code of length specified in the parameter
const getRandomHex = (length) => {
    // Start with a blank string
    let result = "";
    // loop a number of times according to the length parameter
    for (let i = 0; i < length; i++) {
        // assigns a random hex-digit (including 0) to digit
        let digit = (Math.random() * 16 | 0).toString(16);
        // adds digit to the result string
        result += digit;
    }
    return result;
}

// takes parameters int(numberOfAttempts)
const findTheJackpot = (numberOfAttempts, numberToBeat, charToMatch=undefined) => {
    let defaultChecker = charToMatch === undefined;
    let matches = [];
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
            matches.push(hexCode);
        }
    }
    return matches;
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
        for (let j = 0; j < numberToBeat; j++) {
            if (hexCode[j] == charToMatch) {
                numberToWin++;
            }
        }
        if (numberToWin == numberToBeat) {
            let attempts = i == 1 ? "attempt" : "attempts";
            let formattedI = String(i).replace(/(.)(?=(\d{3})+$)/g,'$1,')
            return `It took ${formattedI} ${attempts} to find this hexadecimal number: ${hexCode}`;
        }
        else {
            numberToWin = 0;
            i++;
        }
    }
}

print(findTheJackpot(1000, 3));
print(howManyToTheJackpot(5, "7"));