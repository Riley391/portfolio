// I'm tired of getting confused between Python and JS so I imported my own print() function
const { print } = require("./module");

// Generates a hex-code of length specified in the parameter
const getRandomHex = (length) => {
    // Start with a blank string
    let result = "";
    // loop a number of times according to the length parameter
    for (let i = 0; i < length; i++) {
        // assigns a random hex-digit (including 0) to digit
        let digit = ((Math.random() * 16) | 0).toString(16);
        // adds digit to the result string
        result += digit;
    }
    return result;
};

/* takes parameters int(numberOfAttempts), int(numberToBeat), and string(charToMatch) and 
attempts to find a randomly generated string with the specified number (numberToBeat) 
of a single character (charToMatch) all within the specified number of attempts (numberOfAttempts) */
const findTheJackpot = (numberOfAttempts, numberToBeat, charToMatch = undefined) => {
    // check whether charToMatch was left unassigned and assign resulting boolean to defaultChecker
    let defaultChecker = typeof charToMatch === undefined;
    // array of matches which will eventually be returned
    let matches = [];
    // loop this code as many times as specified by numberOfAttempts
    for (let i = 0; i < numberOfAttempts; i++) {
        // get a random hexcode of length determined by numberToBeat and assign that value to hexCode
        let hexCode = getRandomHex(numberToBeat);
        // if charToMatch was left as the default, assign the first character of the random code to it
        if (defaultChecker) {
            charToMatch = hexCode[0];
        }
        // declare variable to track number of character matches
        let numberToWin = 0;
        // loop through each character in hexCode
        for (let i = 0; i < hexCode.length; i++) {
            // If the character is a match, add 1 to numberToWin
            if (hexCode[i] == charToMatch) {
                numberToWin++;
            }
        }
        // Check to see if the threshold is met
        if (numberToWin == numberToBeat) {
            // If so, add it to the matches array
            matches.push(hexCode);
        }
    }
    return matches;
};

// Same functionality as the previous function, except that this function 
// runs until it finds a match and then returns the number of attempts required to reach it
const howManyToTheJackpot = (numberToBeat, charToMatch = undefined) => {
    let defaultChecker = typeof charToMatch === undefined;
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
            let formattedI = String(i).replace(/(.)(?=(\d{3})+$)/g, "$1,");
            return `It took ${formattedI} ${attempts} to find this hexadecimal number: ${hexCode}`;
        } else {
            numberToWin = 0;
            i++;
        }
    }
};

print(findTheJackpot(1000, 3));
print(howManyToTheJackpot(5, "7"));
