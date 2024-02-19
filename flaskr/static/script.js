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
getInventories();















//fetches the board from app.py
function getBoard(){
    //requests a promise from get_board
    fetch("/get_board")
    .then(res => { //catches promise and parses json
        return res.json();
    })
    .then(data => { //catches json and prints board
        printBoard(data);
    })
    .catch(error => console.log(error));
}

//fetches the inventories
function getInventories(){

    fetch("/get_inventories")
    .then(res => { //catches promise and parses json
        return res.json();
    })
    .then(data => { //catches json and prints board
        printInventories(data);
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

//clears the board
function clearBoard(){
    let table = document.querySelector("table");
    table.innerHTML = '';
}

//prints the board
function printBoard(data){
    let table = document.querySelector("board"); // gets the table class from the html file and turns it into an object
    
        
        for (const outerList of data.board) {
            // Iterate through each inner list
            for (const innerList of outerList) {
              // Iterate through each element in the inner list
                const square = document.createElement('div');//creates a div html object
                square.className = 'table-item';//sets the class name of the div
                square.append(innerList[0]);//adds the value of the square into the html
                board.appendChild(square);//sends the div obj to the html file to be inserted
                // Perform your actions with each element here
            }
          }
}

function printInventories(data){
    let inventoryOne = document.querySelector("playerOne");

        for(const piece of data.one){
            const piecePlacer = document.createElement('div');
            piecePlacer.className = 'piece';
            piecePlacer.append(piece);
            playerOne.appendChild(piecePlacer);
        }
        
    let inventoryTwo = document.querySelector("playerTwo");

        for(const piece of data.two){
            const piecePlacer = document.createElement('div');
            piecePlacer.className = 'piece';
            piecePlacer.append(piece);
            playerTwo.appendChild(piecePlacer);
        }
}

