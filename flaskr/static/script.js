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


//prints the inventories of the players
function printInventories(data){
    //creating a object that allows us to write to the playerOne div in hmtl
    let inventoryOne = document.querySelector("playerOne");

        //for each element in the players inventories, we write the name of the piece to player ones inventory
        for(const piece of data.one){
            //creates a img element and sets the src to the correct image using getImageLight
            const pieceImage = document.createElement('img');
            pieceImage.setAttribute("draggable", "true");
            pieceImage.setAttribute("src", getImageLight(piece));
            pieceImage.setAttribute("style", "padding: 5px");
            
            playerOne.appendChild(pieceImage);
            
        }
    
    //creating a object that allows us to write to the playerTwo div in hmtl
    let inventoryTwo = document.querySelector("playerTwo");

        //for each element in the players inventories, we write the name of the piece to player ones inventory
        for(const piece of data.two){
            //creates a div element and calls it piece it then places the piece name into the div and appends that to the inventory div
            const pieceImage = document.createElement('img');
            pieceImage.setAttribute("draggable", "true");
            pieceImage.setAttribute("src", getImageDark(piece));
            pieceImage.setAttribute("style", "padding: 5px");
            playerTwo.appendChild(pieceImage);
        }
}



function getImageLight(piece){
    switch(piece){
        case 'tavern-1':
            return "static/images/tavern_light.png";

        case 'tavern-2':
            return "static/images/tavern_light.png";

        case 'stable-1':
            return "static/images/stable_light.png";

        case 'stable-2':
            return "static/images/stable_light.png";

        case 'inn-1':
            return "static/images/inn_light.png";

        case 'inn-2':
            return "static/images/inn_light.png";

        case 'bridge':
            return "static/images/bridge_light.png";

        case 'square':
            return "static/images/square_light.png";

        case 'abbey-light':
            return "static/images/abbey_light.png";

        case 'manor':
            return "static/images/manor_light.png";

        case 'tower':
            return "static/images/tower_light.png";

        case 'infirmary':
            return "static/images/infirmary_light.png";

        case 'castle':
            return "static/images/castle_light.png";

        case 'academy-light':
            return "static/images/academy_light.png";

        case 'cathedral':
            return "static/images/cathedral.png";
    }
}

function getImageDark(piece){
    switch(piece){
        case 'tavern-1':
            return "static/images/tavern_dark.png";

        case 'tavern-2':
            return "static/images/tavern_dark.png";

        case 'stable-1':
            return "static/images/stable_dark.png";

        case 'stable-2':
            return "static/images/stable_dark.png";

        case 'inn-1':
            return "static/images/inn_dark.png";

        case 'inn-2':
            return "static/images/inn_dark.png";

        case 'bridge':
            return "static/images/bridge_dark.png";

        case 'square':
            return "static/images/square_dark.png";

        case 'abbey-dark':
            return "static/images/abbey_dark.png";

        case 'manor':
            return "static/images/manor_dark.png";

        case 'tower':
            return "static/images/tower_dark.png";

        case 'infirmary':
            return "static/images/infirmary_dark.png";

        case 'castle':
            return "static/images/castle_dark.png";

        case 'academy-dark':
            return "static/images/academy_dark.png";
    }
}