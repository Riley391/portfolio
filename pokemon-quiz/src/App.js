import "./styles.css";
import { useState } from "react";
import {
  kantoArray,
  johtoArray,
  hoennArray,
  sinnohArray,
  unovaArray,
  kalosArray,
  alolaArray,
  unknownArray,
  galarArray,
  hisuiArray,
  paldeaArray
} from "./pokemonArray.js";

const genArray = [
  kantoArray,
  johtoArray,
  hoennArray,
  sinnohArray,
  unovaArray,
  kalosArray,
  alolaArray,
  unknownArray,
  galarArray,
  hisuiArray,
  paldeaArray
];

const regionArray = [
  "Kanto",
  "Johto",
  "Hoenn",
  "Sinnoh",
  "Unova",
  "Kalos",
  "Alola",
  "Unknown",
  "Galar",
  "Hisui",
  "Paldea"
];

export default function App() {
  const [checkBoxStates, setCheckBoxStates] = useState(Array(11).fill(true));
  const [pokeList, setPokeList] = useState(null);
  const [textBoxValue, setTextBoxValue] = useState("");
  const [pokeListLength, setPokeListLength] = useState(null);
  const [size, setSize] = useState(70);
  const [count, setCount] = useState(0);
  const [isCounting, setIsCounting] = useState(false);
  const [clock, setClock] = useState(null);

  let imagesArray = [];
  let currentListLength = null;
  let numberGuessed = null;
  let percentGuessed = null;
  if (pokeList) {
    imagesArray = pokeList.map((pokemon) => (
      <img
        key={pokemon}
        id={pokemon}
        className="poke-pic"
        src={
          "images/" +
          pokemon
            .toLowerCase()
            .replace(".", "")
            .replace("'", "")
            .replace(":", "")
            .replace(" ", "-") +
          ".jpg"
        }
        alt={pokemon}
        style={{ width: size.toString() + "px" }}
      />
    ));
    currentListLength = pokeList.length;
    numberGuessed = pokeListLength - currentListLength;
    percentGuessed = Math.round((numberGuessed / pokeListLength) * 1000) / 10;
  }

  function startCount() {
    setCount(0);
    const clock = setInterval(() => setCount((count) => count + 1), 1000);
    setIsCounting(true);
    return clock;
  }

  function resetCount() {
    setCount(0);
  }

  function stopCount(clock) {
    clearInterval(clock);
    setIsCounting(false);
  }

  function buildTime(count) {
    const seconds = count % 60;
    const minutes = Math.trunc(count / 60) % 60;
    const hours = Math.trunc(count / 3600);
    const minutesString =
      minutes >= 10 ? minutes.toString() : "0" + minutes.toString();
    const secondsString =
      seconds >= 10 ? seconds.toString() : "0" + seconds.toString();
    return hours.toString() + ":" + minutesString + ":" + secondsString;
  }

  function handleCheck(i) {
    const newChecks = [...checkBoxStates];
    newChecks[i] = !checkBoxStates[i];
    setCheckBoxStates(newChecks);
  }

  function buildPokeList() {
    const result = [];
    for (let i = 0; i < checkBoxStates.length; i++) {
      if (checkBoxStates[i]) {
        result.push(...genArray[i]);
      }
    }
    setPokeListLength(result.length);
    return result;
  }

  return (
    <div className="App">
      <h1>Pokémon Quiz</h1>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          marginBottom: "25px"
        }}
      >
        <fieldset>
          <legend>Pokémon Generation Selector:</legend>
          <div className="gen-selector-box">
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[0].toLowerCase()}
                name={regionArray[0].toLowerCase()}
                checked={checkBoxStates[0]}
                onChange={() => handleCheck(0)}
              />
              <label htmlFor={regionArray[0].toLowerCase()}>
                {regionArray[0]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[1].toLowerCase()}
                name={regionArray[1].toLowerCase()}
                checked={checkBoxStates[1]}
                onChange={() => handleCheck(1)}
              />
              <label htmlFor={regionArray[1].toLowerCase()}>
                {regionArray[1]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[2].toLowerCase()}
                name={regionArray[2].toLowerCase()}
                checked={checkBoxStates[2]}
                onChange={() => handleCheck(2)}
              />
              <label htmlFor={regionArray[2].toLowerCase()}>
                {regionArray[2]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[3].toLowerCase()}
                name={regionArray[3].toLowerCase()}
                checked={checkBoxStates[3]}
                onChange={() => handleCheck(3)}
              />
              <label htmlFor={regionArray[3].toLowerCase()}>
                {regionArray[3]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[4].toLowerCase()}
                name={regionArray[4].toLowerCase()}
                checked={checkBoxStates[4]}
                onChange={() => handleCheck(4)}
              />
              <label htmlFor={regionArray[4].toLowerCase()}>
                {regionArray[4]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[5].toLowerCase()}
                name={regionArray[5].toLowerCase()}
                checked={checkBoxStates[5]}
                onChange={() => handleCheck(5)}
              />
              <label htmlFor={regionArray[5].toLowerCase()}>
                {regionArray[5]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[6].toLowerCase()}
                name={regionArray[6].toLowerCase()}
                checked={checkBoxStates[6]}
                onChange={() => handleCheck(6)}
              />
              <label htmlFor={regionArray[6].toLowerCase()}>
                {regionArray[6]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[7].toLowerCase()}
                name={regionArray[7].toLowerCase()}
                checked={checkBoxStates[7]}
                onChange={() => handleCheck(7)}
              />
              <label htmlFor={regionArray[7].toLowerCase()}>
                {regionArray[7]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[8].toLowerCase()}
                name={regionArray[8].toLowerCase()}
                checked={checkBoxStates[8]}
                onChange={() => handleCheck(8)}
              />
              <label htmlFor={regionArray[8].toLowerCase()}>
                {regionArray[8]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[9].toLowerCase()}
                name={regionArray[9].toLowerCase()}
                checked={checkBoxStates[9]}
                onChange={() => handleCheck(9)}
              />
              <label htmlFor={regionArray[9].toLowerCase()}>
                {regionArray[9]}
              </label>
            </div>
            <div className="poke-check-box">
              <input
                type="checkbox"
                id={regionArray[10].toLowerCase()}
                name={regionArray[10].toLowerCase()}
                checked={checkBoxStates[10]}
                onChange={() => handleCheck(10)}
              />
              <label htmlFor={regionArray[10].toLowerCase()}>
                {regionArray[10]}
              </label>
            </div>
          </div>
          <button
            onClick={() => {
              setPokeList(buildPokeList());
              if (isCounting) {
                resetCount();
              } else {
                setClock(startCount());
              }
            }}
            style={{
              marginTop: "6px",
              padding: "5px 8px",
              borderRadius: "10px"
            }}
          >
            Start
          </button>
        </fieldset>
      </div>
      {pokeList ? (
        <div>
          <div>
            <div
              style={{
                fontWeight: "bold",
                fontSize: "30px",
                marginTop: "10px"
              }}
            >
              {buildTime(count)}
            </div>
          </div>
          <div>
            <div style={{ margin: "10px" }}>
              {numberGuessed} out of {pokeListLength} guessed (
              {currentListLength} left, {percentGuessed}% done)
            </div>
          </div>
          <div>
            <div>
              <input
                type="text"
                value={textBoxValue}
                onChange={(e) => {
                  setTextBoxValue(e.target.value);
                  let tempList = [];
                  if (e.target.value.toLowerCase() === "nidoran") {
                    if (pokeList.indexOf("Nidoran-M") !== -1) {
                      const tempList = [...pokeList];
                      tempList.splice(tempList.indexOf("Nidoran-M"), 1);
                      tempList.splice(tempList.indexOf("Nidoran-F"), 1);
                      setPokeList(tempList);
                      setTextBoxValue("");
                    }
                  }
                  for (let i = 0; i < pokeList.length; i++) {
                    if (
                      e.target.value.toLowerCase() === pokeList[i].toLowerCase()
                    ) {
                      tempList = [...pokeList];
                      tempList.splice(i, 1);
                      setPokeList(tempList);
                      setTextBoxValue("");
                      if (tempList.length === 0) {
                        stopCount(clock);
                      }
                    }
                  }
                }}
                style={{ marginBottom: "5px" }}
              />
            </div>
          </div>
          <div>
            <input
              type="range"
              min="20"
              max="700"
              value={size}
              onChange={(e) => setSize(e.target.value)}
            />
          </div>
          {imagesArray}
        </div>
      ) : (
        <></>
      )}
      {percentGuessed === 100 ? (
        <h2>Congratulations! You guessed them all!</h2>
      ) : (
        <></>
      )}
    </div>
  );
}
