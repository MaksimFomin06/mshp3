"use strict"

function getNotes() {
    let request = new XMLHttpRequest();
    request.open("GET", "/get_notes/", true);
    request.onload = function () {
        console.log("Я получило ответ от сервера!");

        let responseJSON = JSON.parse(request.response);
        console.log(responseJSON);

        let notesList = document.querySelector("#notesList");
        notesList.innerHTML = "";
        for (let index = 0; index < responseJSON.notes.length; ++index) {
            notesList.innerHTML += `<li>${responseJSON.notes[index]}</li>`
        }
    };

    request.send();
}

function postNote() {
    let request = new XMLHttpRequest();
    request.open("POST", "/", true);
    request.onload = function () {
        console.log("Я получил ответ!");
    };

    let noteText = document.querySelector("#noteText").value;
    let csrfToken = Cookies.get("csrftoken");
    request.setRequestHeader("X-CSRFToken", csrfToken);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send("noteText=" + noteText);
}


let buttonGetNotes = document.querySelector("#buttonGetNotes");
buttonGetNotes.addEventListener("click", getNotes);
let buttonPostNote = document.querySelector("#buttonPostNote");
buttonPostNote.addEventListener("click", postNote);