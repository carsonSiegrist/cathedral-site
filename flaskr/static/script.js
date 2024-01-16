//calls getBoard function
fetch("/start_game", {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    // You can include a request body if needed
    // body: JSON.stringify({ key: 'value' })
})
.then(response => response.json())
.then(data => {
    console.log(data.message); // Log the message received from the server
    // Further actions based on the response, if needed
})
.catch(error => console.error('Error:', error));

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
    let pieceData = {
        piece: document.getElementById('Piece').value,
        rotation: document.getElementById('rotation').value,
        coordinate: [document.getElementById('xCord').value, document.getElementById('yCord').value]
    }
    

    //posts the player information to app.py
    fetch('/play_move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(pieceData)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    
}

function boardClick(){
    clearBoard();
    getBoard();
}
function clearBoard(){
    let table = document.querySelector("table");
    table.innerHTML = '';
}

//prints the board
function printBoard(data){
    let table = document.querySelector("table"); // gets the table class from the html file and turns it into an object
    
        /*for(let row of data){
            for(let val of row){//we go through the json file value by value and print it to the html file by creating a div object and pushing it to the table object
                const square = document.createElement('div');
                square.className = 'table-item';
                square.append(val[0]);
                table.appendChild(square);
            }
        }*/
        for (const outerList of data.board) {
            // Iterate through each inner list
            for (const innerList of outerList) {
              // Iterate through each element in the inner list
                const square = document.createElement('div');
                square.className = 'table-item';
                square.append(innerList[0]);
                table.appendChild(square);
                // Perform your actions with each element here
            }
          }
}