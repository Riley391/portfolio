let selectedColor;
let previousColor;

const getRandomHex = () => {
    let randomColor = Math.floor(Math.random()*16777215).toString(16);
    while (randomColor.length < 6) {
        randomColor = "0" + randomColor;
    }
    return "#" + randomColor;
}

const changeColor = i => {
    const el = document.getElementById(`pixel${i}`);

    if (selectedColor === undefined) {
        el.style.backgroundColor = getRandomHex();
    }
    el.style.backgroundColor = selectedColor;
}

const selectColor = color => {
    const el = document.getElementById(color);

    if (previousColor !== undefined) {
        previousColor.style.height = "33px";
        previousColor.style.width = "33px";
        previousColor.style.border = "none";
    }
    selectedColor = color;
    el.style.height = "31px";
    el.style.width = "31px";
    el.style.border = "1px solid black";
    previousColor = el;
}

const shuffle = () => {
    for (let i = 1; i <= 10000; i++) {
        document.getElementById(`pixel${i}`).style.backgroundColor = getRandomHex();
    }
}

const startUp = () => {
    populateCanvas();
    populatePalette();
}

const populateCanvas = () => {
    for (let i = 1; i <= 10000; i++) {
        const el = document.createElement("div");
        el.setAttribute('id', `pixel${i}`);
        el.setAttribute('class', 'pixel');
        el.setAttribute('onclick', `changeColor(${i})`);

        document.getElementById("canvas").appendChild(el);
    }
}

const populatePalette = () => {
    let colorArray = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'white', 'black', 'maroon', 'brown', 'yellowgreen', 'lightgreen', 'lightblue', 'purple', 'pink', 'lightgray', 'darkgray'];
    for (let i = 0; i < 18; i++) {
        const el = document.createElement("div");
        el.setAttribute('class', 'color');
        el.setAttribute('id', `${colorArray[i]}`);
        el.setAttribute('onclick', `selectColor('${colorArray[i]}')`);
        //el.addEventListener('click', selectColor(colorArray[i]));
        el.style.backgroundColor = colorArray[i];

        document.getElementById("palette").appendChild(el);
    }
}

function coolDownTimer() {
    //TODO: add a cooldown timer
}

//TODO: add persistent data with mySQL and PHP
//TODO: try adding persistent data using JSON