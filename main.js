"use strict";

let nRows = null;
let nCols = null;

function loadFile(file) {
    const grid = document.getElementById("grid");
    grid.innerHTML = "";

    console.log(file);
    file.text().then(text => {
        const tiles = JSON.parse(text);

        const nCols = Math.max(...tiles.map(tile => tile.column)) + 1;
        const nRows = Math.max(...tiles.map(tile => tile.row)) + 1;

        console.log(tiles, nCols, nRows);

        for (let r = 0; r < nRows; r++) {
            for (let c = 0; c < nCols; c++) {
                const tile = tiles.filter(tile => tile.row === r && tile.column === c)[0];
                const child = document.createElement("div");

                child.id = `R${r}C${c}`;
                child.classList.add("tile", tile.type);
                child.setAttribute("row", `${r}`);
                child.setAttribute("col", `${c}`);

                child.addEventListener("click", tileOnClick);

                grid.appendChild(child);
            }
        }

        grid.style.gridTemplateColumns = "auto ".repeat(nCols);
        grid.style.gridTemplateRows = "auto ".repeat(nRows);
    });

    afterTile();
}

function generate() {
    nRows = document.getElementById("n-rows").value;
    nCols = document.getElementById("n-cols").value;

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

    afterTile();
}


function afterTile() {
    document.getElementById("generate").setAttribute("disabled", "disabled");
    document.getElementById("n-rows").setAttribute("disabled", "disabled");
    document.getElementById("n-cols").setAttribute("disabled", "disabled");
    document.getElementById("fileInput").setAttribute("disabled", "disabled");

    document.getElementById("downloadJson").removeAttribute("disabled");
    document.getElementById("downloadProblem").removeAttribute("disabled");
}

function tileOnClick(ev) {
    const tile = ev.target;
    const tileType = getType(tile);

    let nextClass;
    if (tileType === "road")
        nextClass = "parking";
    else if (tileType === "parking")
        nextClass = "blocked";
    else if (tileType === "blocked")
        nextClass = "hub";
    else if (tileType === "hub")
        nextClass = "road";
    else
        alert("unknown tile type!");

    tile.classList.remove("road", "parking", "hub", "blocked");
    tile.classList.add(nextClass);
}

function getType(tile) {
    if (tile.classList.contains("road")) return "road";
    if (tile.classList.contains("parking")) return "parking";
    if (tile.classList.contains("blocked")) return "blocked";
    if (tile.classList.contains("hub")) return "hub";
}


function dumpJson() {
    const jsonDump = [];

    for (let r = 0; r < nRows; r++) {
        for (let c = 0; c < nCols; c++) {
            const tile = document.getElementById(`R${r}C${c}`);
            jsonDump.push({
                row: r,
                column: c,
                type: getType(tile),
            });
        }
    }

    return JSON.stringify(jsonDump);
}

function downloadJsonDump() {
    const jsonDump = dumpJson();
    download("map.json", jsonDump);
}


function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}


function dumpProblem() {
    let tiles = "";
    let leftOfs = "";
    let aboves = "";

    for (let r = 0; r < nRows; r++) {
        for (let c = 0; c < nCols; c++) {
            const tile = document.getElementById(`R${r}C${c}`);
            tiles += `        R${r}C${c} - ${getType(tile)}Tile\n`;
            if (r > 0)
                aboves += `        (IsAbove R${r - 1}C${c} R${r}C${c})\n`;
            if (c > 0)
                leftOfs += `        (IsToTheLeftOf R${r}C${c - 1} R${r}C${c})\n`;
        }
    }

    return `
;; Authors: Theodor Amariucai & Bora M. Alper (in no particular order)

(define (problem waiting-XX)
    (:domain finitech)
    (:objects
        {{ objects }}

        ;; Generated by Finitech Map Editor by Bora M. Alper
${tiles}
    )

    (:init
        {{ init }}
        

        ;; Generated by Finitech Map Editor by Bora M. Alper
${leftOfs}
${aboves}
    )

    (:goal (and
        (not (exists (?c - car) (or
            (AwaitingParking ?c)
            (AwaitingDelivery   ?c)
        )))
    ))
)
`
}

function downloadProblem() {
    download("problem.pddl.mustache", dumpProblem());
}
