"use strict";

const predicates = document.getElementById("predicates");
const objects = document.getElementById("objects");

resetOutput();

function generate() {
    const nRows = document.getElementById("n-rows").value;
    const nCols = document.getElementById("n-cols").value;

    const grid = document.getElementById("grid");
    grid.innerHTML = "";

    for (let r = 0; r < nRows; r++) {
        for (let c = 0; c < nCols; c++) {
            const child = document.createElement("div");

            child.id = `R${r}C${c}`;
            child.classList.add("tile", "road");
            child.setAttribute("row", `${r}`);
            child.setAttribute("col", `${c}`);

            child.addEventListener("click", tileOnClick);

            grid.appendChild(child);
        }
    }

    grid.style.gridTemplateColumns = "auto ".repeat(nCols);
    grid.style.gridTemplateRows = "auto ".repeat(nRows);
}


function tileOnClick(ev) {
    const tile = ev.target;
    const tileType = getType(tile);

    let nextClass;
    if (tileType === "road")
        nextClass = "park";
    else if (tileType === "park")
        nextClass = "dropoff";
    else if (tileType === "dropoff")
        nextClass = "pickup";
    else if (tileType === "pickup")
        nextClass = "road";

    tile.classList.remove("road", "park", "dropoff", "pickup");
    tile.classList.add(nextClass);
}

function getType(tile) {
    if (tile.classList.contains("road")) return "road";
    if (tile.classList.contains("park")) return "park";
    if (tile.classList.contains("dropoff")) return "dropoff";
    if (tile.classList.contains("pickup")) return "pickup";
}

function dump() {
    const nRows = document.getElementById("n-rows").value;
    const nCols = document.getElementById("n-cols").value;

    resetOutput();

    for (let r = 0; r < nRows; r++) {
        for (let c = 0; c < nCols; c++) {
            const tile = document.getElementById(`R${r}C${c}`);

            if (r > 0)
                emit_isToTheUp(`R${r - 1}C${c}`, `R${r}C${c}`);
            if (c > 0)
                emit_isToTheLeft(`R${r}C${c - 1}`, `R${r}C${c}`);

            emit_object_tile(`R${r}C${c}`, getType(tile));
        }
    }
}

function resetOutput() {
    predicates.value = "";
    objects.value = "";
}

function emit_isToTheLeft(a, b) {
    predicates.value += `        (IsToTheLeft ${a} ${b})\n`;
}

function emit_isToTheUp(a, b) {
    predicates.value += `        (IsToTheUp ${a} ${b})\n`;
}

function emit_object_tile(o, type) {
    objects.value += `        ${o} - ${type}\n`;
}
