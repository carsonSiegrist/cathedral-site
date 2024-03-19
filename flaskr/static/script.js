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

//clears the board
function clearBoard(){
    let table = document.querySelector(".board");
    table.innerHTML = '';
    console.log("Cleared board");
}

//prints the board
function printBoard(data){
    console.log(data);
    let table = document.querySelector(".board"); // gets the table class from the html file and turns it into an object
    
        
        for (const outerList of data.board) {
            // Iterate through each inner list
            for (const innerList of outerList) {
              // Iterate through each element in the inner list
                const square = document.createElement('div');//creates a div html object
                square.className = 'table-item';//sets the class name of the div
                if(innerList[0] == 1){
                    square.style.backgroundColor = "grey";
                }
                else if(innerList[0] == 2){
                    square.style.backgroundColor = "rgb(233, 177, 131)";
                }
                else if(innerList[0] == 3){
                    square.style.backgroundColor = "rgb(53, 26, 4)";
                }

                
                //adds the value of the square into the html
                board.appendChild(square);//sends the div obj to the html file to be inserted
                // Perform your actions with each element here
            }
          }
}

//clears the inventories of the players
function clearInventories(){
    let InventoryOne = document.querySelector(".playerOne");
    InventoryOne.innerHTML = '';

    let InventoryTwo = document.querySelector(".playerTwo");
    InventoryTwo.innerHTML = '';

    console.log("Cleared inventories");
}

//prints the inventories of the players
function printInventories(data){
    //creating a object that allows us to write to the playerOne div in hmtl
    let inventoryOne = document.querySelector("playerOne");
    let inventoryOneName = document.querySelector(".playerOne");
    inventoryOneName.innerHTML = '<h3>Player One</h3>';
        //for each element in the players inventories, we write the name of the piece to player ones inventory
        for(const piece of data.one){
            //creates a img element and sets the src to the correct image using getImageLight
            const pieceImage = document.createElement('img');
            pieceImage.className = piece;
            pieceImage.setAttribute("draggable", "true");
            pieceImage.setAttribute("src", getImageLight(piece));
            pieceImage.setAttribute("style", "padding: 5px");
            
            playerOne.appendChild(pieceImage);
            
        }
    
    //creating a object that allows us to write to the playerTwo div in hmtl
    let inventoryTwo = document.querySelector("playerTwo");
    let inventoryTwoName = document.querySelector(".playerTwo");
    inventoryTwoName.innerHTML = '<h3>Player Two</h3>';
        //for each element in the players inventories, we write the name of the piece to player ones inventory
        for(const piece of data.two){
            //creates a div element and calls it piece it then places the piece name into the div and appends that to the inventory div
            const pieceImage = document.createElement('img');
            pieceImage.className = piece;
            pieceImage.setAttribute("draggable", "true");
            pieceImage.setAttribute("src", getImageDark(piece));
            pieceImage.setAttribute("style", "padding: 5px");
            playerTwo.appendChild(pieceImage);
        }
}


//finds correct image link corresponding to piece name
function getImageLight(piece){
    switch(piece){
        case 'tavern-1':
            return "static/images/tavern_light_1.png";
        case 'tavern-2':
            return "static/images/tavern_light_2.png";

        case 'stable-1':
            return "static/images/stable_light_1.png";
        case 'stable-2':
            return "static/images/stable_light_2.png";

        case 'inn-1':
            return "static/images/inn_light_1.png";
        case 'inn-2':
            return "static/images/inn_light_2.png";

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
            return "static/images/tavern_dark_1.png";
        case 'tavern-2':
            return "static/images/tavern_dark_2.png";

        case 'stable-1':
            return "static/images/stable_dark_1.png";
        case 'stable-2':
            return "static/images/stable_dark_2.png";

        case 'inn-1':
            return "static/images/inn_dark_1.png";
        case 'inn-2':
            return "static/images/inn_dark_2.png";

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



document.querySelector(".board").addEventListener("dragover", function (event) {
    event.preventDefault();
});

let mouseX = 0;
let mouseY = 0;
let rotation = 0;

function onDrag(event) {
    if (event.shiftKey) {
        
        rotatePiece();
    }
}

// Add mousemove event listener to the board to track mouse position
document.querySelector(".board").addEventListener("mousemove", function(event) {
    // Update mouse coordinates relative to the board
    const boardRect = event.currentTarget.getBoundingClientRect();
    mouseX = event.clientX - boardRect.left + window.scrollX;
    mouseY = event.clientY - boardRect.top + window.scrollY;
});

function updateBoardSize() {
    // Get the container element
    const container = document.querySelector(".container");
    
    // Get the width of the container
    const containerWidth = container.clientWidth;

    // Calculate the width and height of the grid area based on the column and row spans
    const gridAreaWidth = (containerWidth / 4) * 2; // Assuming 2 columns in the middle
    const gridAreaHeight = gridAreaWidth; // Assuming 1 row in the middle

    // Set the width and height of the board to match the grid area size
    const board = document.querySelector(".board");
    board.style.width = gridAreaWidth + "px";
    board.style.height = gridAreaHeight + "px";
}

// Call the updateBoardSize function when the page loads and whenever the window is resized
window.addEventListener("load", updateBoardSize);
window.addEventListener("resize", updateBoardSize);


document.addEventListener('keydown', function(event) {
    // Check if the pressed key is 'r'
    if (event.key === 'r') {
        rotatePiece();
    }
});


// Add drop event listener to the board
// Add drop event listener to the board
document.querySelector(".board").addEventListener("drop", function (event) {
    event.preventDefault();
    
    // Get the board element
    const board = document.querySelector(".board");
    
    // Get the bounding rectangle of the board
    const boardRect = board.getBoundingClientRect();
    
    // Calculate the dimensions of each cell
    const cellWidth = board.clientWidth / 10; // Assuming 10 columns
    const cellHeight = board.clientHeight / 10; // Assuming 10 rows
    
    // Calculate the mouse coordinates relative to the board
    const mouseX = event.clientX - boardRect.left;
    const mouseY = event.clientY - boardRect.top;
    
    // Calculate the row and column indices
    const col = Math.floor(mouseX / cellWidth);
    const row = Math.floor(mouseY / cellHeight);

    console.log("MouseX: " + mouseX + " MouseY: " + mouseY);
    console.log("BoardRect: ", boardRect);
    console.log("CellWidth: " + cellWidth + " CellHeight: " + cellHeight);
    console.log("Calculated Row: " + row + " Calculated Column: " + col);

    // Grab the link of the object dropped and parse it to get the name of the item
    const draggedPieceName = event.dataTransfer.getData("text/plain");
    
    let urlParts = draggedPieceName.split('/');
    // Get the last part of the URL (which should be the filename)
    let fileNameWithExtension = urlParts[urlParts.length - 1];
    
    console.log("Piece: " + fileNameWithExtension + " rotation val: " + 0 + " row: " + row + " column: " + col);

    let pieceData = {
        piece: getImageInfo(fileNameWithExtension),
        rotation: rotation,
        coordinate: [col, row]
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
            clearBoard();
            getBoard();
            clearInventories();
            getInventories();
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

function rotatePiece(){
    if(rotation == 3)
            rotation = 0;
        else
            rotation++;
}
//finds correct piece name corresponding to image link
function getImageInfo(piece){
    switch(piece){
        case 'tavern_light_1.png':
            return "tavern-1";
        case 'taver_light_2.png':
            return "tavern-2";

        case 'stable_light_1.png':
            return "stable-1";
        case 'stable_light_2.png':
            return "stable-2";

        case 'inn_light_1.png"':
            return "inn-1";
        case 'inn_light_2.png"':
            return "inn-2";

        case 'bridge_light.png':
            return "bridge";

        case 'square_light.png':
            return "square";

        case 'abbey_light.png':
            return "abbey-light";

        case 'manor_light.png':
            return "manor";

        case 'tower_light.png':
            return "tower";

        case 'infirmary_light.png':
            return "infirmary";

        case 'castle_light.png':
            return "castle";

        case 'academy_light.png':
            return "academy-light";

        case 'cathedral.png':
            return "cathedral";



        case 'tavern_dark_1.png':
            return "tavern-1";
        case 'taver_dark_2.png':
            return "tavern-2";

        case 'stable_dark_1.png':
            return "stable-1";
        case 'stable_dark_2.png':
            return "stable-2";

        case 'inn_dark_1.png"':
            return "inn-1";
        case 'inn_dark_2.png"':
            return "inn-2";

        case 'bridge_dark.png':
            return "bridge";

        case 'square_dark.png':
            return "square";

        case 'abbey_dark.png':
            return "abbey-dark";

        case 'manor_dark.png':
            return "manor";

        case 'tower_dark.png':
            return "tower";

        case 'infirmary_dark.png':
            return "infirmary";

        case 'castle_dark.png':
            return "castle";

        case 'academy_dark.png':
            return "academy-dark";
    }
}