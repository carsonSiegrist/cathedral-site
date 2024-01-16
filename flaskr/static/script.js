//calls getBoard function
getBoard();

//fetches the board from app.py
function getBoard(){
    //requests a promise from get_board
    fetch("/get_board")
    .then(res => { //this catches a promise if it comes in, if it does come in, it parses the json file so that we can read it
        return res.json();
    })
    .then(data => {
        printBoard(data);
    })
    .catch(error => console.log(error));
}

//this runs when the play button is pressed
function onClick(){
    //this gets the data from the dropdown menus
    const piece = document.getElementById('Piece').value;
    const rotation = document.getElementById('rotation').value;
    
    //posts the player information to app.py
    fetch("")
}

function clearBoard(){
    let table = document.querySelector("table");
    table.innerHTML = '';
}

//prints the board
function printBoard(data){
    let table = document.querySelector("table"); // gets the table class from the html file and turns it into an object

        for(let row of data){
            for(let val of row){//we go through the json file value by value and print it to the html file by creating a div object and pushing it to the table object
                const square = document.createElement('div');
                square.className = 'table-item';
                square.append(val);
                table.appendChild(square);
            }
        }
}