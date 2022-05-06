let boxTicker = 1;
let deleteLimit = 1;
let iteratorMultiplier = 0;
let word = "BLAST";
let keepPlaying = true;
const letters = [];

// Find a better way of converting string to array
for (i = 0; i < word.length; i++) {
    letters[i] = word.substr(i, 1);
}

function displayChar(character) {
    if (keepPlaying) {
        if (boxTicker <= 30) {
            document.getElementById(boxTicker.toString()).innerHTML = character;
            boxTicker ++;
        }
    }
}

function deleteChar() {
    if (keepPlaying) {
        if (boxTicker > deleteLimit) {
            boxTicker --;
            document.getElementById(boxTicker.toString()).innerHTML = "";
        }
    }
}

function enterWord() {
    let playerWord = "";
    const playerArray = [document.getElementById((1 + iteratorMultiplier).toString()).innerHTML,
    document.getElementById((2 + iteratorMultiplier).toString()).innerHTML,
    document.getElementById((3 + iteratorMultiplier).toString()).innerHTML,
    document.getElementById((4 + iteratorMultiplier).toString()).innerHTML,
    document.getElementById((5 + iteratorMultiplier).toString()).innerHTML];

    for (i = 0; i < 5; i++) {
        playerWord = playerWord + playerArray[i];
    }

    if (boxTicker == 6 + iteratorMultiplier) {
        for (i = 1 + iteratorMultiplier; i < 6 + iteratorMultiplier; i++) {
            if (document.getElementById(i.toString()).innerHTML == letters[(i - 1) - iteratorMultiplier]) {
                document.getElementById(i.toString()).style.backgroundColor = "green";
            }
            else {
                turnYellow(i);
                if (document.getElementById(i.toString()).style.backgroundColor != "rgb(182, 167, 34)") {
                    document.getElementById(document.getElementById(i.toString()).innerHTML).innerHTML = "";
                }
            }
        }

        iteratorMultiplier = boxTicker - 1;

        deleteLimit = boxTicker;
    }

    if (playerWord == word) {
        document.getElementById("results").innerHTML = "CONGRATULATIONS! YOU WIN!!";
        keepPlaying = false;
    }
    else if (playerWord != word && boxTicker == 31) {
        document.getElementById("results").innerHTML = "YOU LOSE";
        keepPlaying = false;
    }
}

// TODO: Repeat characters don't count! (Unless they repeat in the hidden word as well)
function turnYellow(i) {
    for (j = 1; j < 6; j++) {
        if (document.getElementById(i.toString()).innerHTML == letters[j - 1]) {
            document.getElementById(i.toString()).style.backgroundColor = "rgb(182, 167, 34)";
        }
    }
}