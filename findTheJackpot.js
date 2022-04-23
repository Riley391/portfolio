const getRandomHex = () => {
    let result = "";
    for (let i = 0; i < 6; i++) {
        let digit = (Math.random() * 16 | 0).toString(16);
        result += digit;
    }
    return result;
}

const findTheJackpot = (numberOfAttempts) => {
    for (let i = 0; i < numberOfAttempts; i++) {
        let hexCode = getRandomHex();
        let charToMatch = hexCode[0];
        let sixToWin = 1;
        for (let i = 1; i < 6; i++) {
            if (hexCode[i] == charToMatch) {
                sixToWin++;
            }
        }
        if (sixToWin == 6) {
            console.log(hexCode);
        }
    }
}

findTheJackpot(1000000)