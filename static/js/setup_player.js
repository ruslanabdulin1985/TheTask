class Setup {
  constructor() {
 this.current_ship = null;
 this.selection = new Selection();
 this.list_of_ships = [];
 this.player = null;
// this.shipSet = getRules();//number of elements: number of ships, values: types of ships
this.shipSet = [1,2];
let name_is_set = false;
let ships_are_set = false;
  }
}

class Player{
constructor(name){
    this.name = name;
}
}

class Selection{
constructor(){
         this.number_of_selected_cells = 0;
         this.lastClickedCellId = null;
    }
}

class Coordinates{
    constructor(x_val, y_val){
         this.x = x_val;
         this.y = y_val;
    }
}

class Ship{
    constructor(type_val){
         this.s_type = type_val;
         this.set_of_coordinates = [];
    }

    add_coordinates(coordinates_obj){
        this.set_of_coordinates.push(coordinates_obj);
    }

    is_allowed(num){
        console.log("num"+num);
        console.log("ss"+this.s_type);
        if (num == this.s_type)
            return true;
        else
           return false;
    }
}

setup = new Setup();

function onlyOneChecked(checkbox) {
/**
 * Allows only one of check boxes be toggled
 * @param  checkbox arg1 checkbox document element
 */
    var checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false;
    })
}

function noneChecked() {
/**
 * makes all the checkbox unchecked
 */
    var checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        item.checked = false;
    })
}


//
//function set_name(player){
///**
// * takes player's name and passes it to the Model through XMLHttpRequest
// *@param player arg1 number of the current player, either 1 or 2
// */
//name = document.getElementById("name").value;
//var xhttp = new XMLHttpRequest();
//    xhttp.onreadystatechange = function() {
//      if (this.readyState == 4 && this.status == 200) {
//        stBtn = document.getElementById("confirmBtn");
//        stBtn.style.cursor= "not-allowed";
//        stBtn.style.pointerEvents= "none";
//        console.log("player "+ player +" name " + name)
//      }
//      }
//    xhttp.open("GET", "/set_name/"+player+"/"+name, true);
//    xhttp.send();
//}

function isNeighbourCell(cell_id, lastChecked){
    if (lastChecked == null)
        return true;

    let letters = ['a','b','c','d','e','f','g','h','i','j'];
    let lastletterIndex = (letters.indexOf(lastChecked[1]));
    let thisletterIndex = (letters.indexOf(cell_id[1]));
    let thisNumberInt = parseInt(cell_id[2], 10);
    let lastNumberInt = parseInt(lastChecked[2], 10);
    if ((lastletterIndex == thisletterIndex+1|| lastletterIndex == thisletterIndex-1)&lastNumberInt == thisNumberInt)
        return true;
    else if ((lastNumberInt == thisNumberInt+1|| lastNumberInt == thisNumberInt-1)&lastletterIndex == thisletterIndex)
        return true;
    else
        return false;
}


function renewBoard(){
    /**
    * Clean the board for a new ship
    */
    let letters = ['a','b','c','d','e','f','g','h','i','j'];

    for (let i=1; i<11; i++){
         for (let j=0; j<10; j++){

            element = document.getElementById('y'+letters[j]+[i])
            if (element.style.backgroundColor=='gray')
                element.style.backgroundColor = 'lightgray';
            }
    }
}

function add_ship(ship_obj){
        setup.list_of_ships.push(ship_obj);
        ship_obj.set_of_coordinates.forEach((item) => {
        element= document.getElementById("y"+item.x+item.y);
        element.style.backgroundColor = 'skyblue';
        console.log(element);
    })

        reNewShip();
        renewBoard();
        noneChecked();
        btn = document.getElementById("confirmShipBtn");
        btn.disabled=true;
        btn.className = "inactive-button";
}

function save_setup(player, setup_obj){
    setup.player = new Player(document.getElementById('name').value);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {

      if (this.readyState == 4 && this.status == 200) {
//            TODO unblock next button
      }
      }
    var data = JSON.stringify(setup_obj);

    xhttp.open("POST", "/save_setup/"+player, true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    console.log(setup.current_ship)
    xhttp.send(data);

}

function reNewShip(){
    setup.shipType = 0;
    setup.shipCellsSet = 0;
    setup.shipCellsSet = 0;
}

function click(event)
        {/**
        *Handles clicks on different elements of UI
        *@param event - event click
        */

            id = event.target.id;
            element = document.getElementById(id);
            //if toggled/untogled checkbox
            if (id!= null && id.match(/^t[1234]$/)!=null){
                console.log(element.checked)
                btn = document.getElementById("confirmShipBtn");
                btn.disabled=true;
                btn.className = "inactive-button";
                 if (element.checked==true){
                    onlyOneChecked(element);
                    reNewShip(); //renews visual atributes of a ship
                    renewBoard(); // renew board
                    setup.current_ship = new Ship(id[1]);
                    console.log(id[1]);
                    setup.selection = new Selection();
                 }
                 else{// unchecked
                    renewBoard(); // renew board
                    setup.current_ship = new Ship(0);
                    setup.selection = new Selection();

                 }

            }

//            if a cell on the board is clicked
            else if (id!= null && id.match(/(^y[a-j](10)$)|(^y[a-j][0123456789]$)/)!=null){
                   if (isNeighbourCell(id, setup.selection.lastClickedCellId)){
                       setup.selection.lastClickedCellId = id;
                       setup.selection.number_of_selected_cells++;

                       if(setup.selection.number_of_selected_cells<=setup.current_ship.s_type){
                           element.style.backgroundColor = 'gray';
                           setup.current_ship.add_coordinates(new Coordinates(id[1], parseInt(id.substring(2), 10)));
                           if (setup.current_ship.is_allowed(setup.selection.number_of_selected_cells)){
                                btn = document.getElementById("confirmShipBtn");
                                btn.disabled=false;
                                btn.className = "confirm-button";
                                }
                           console.log(setup.current_ship.s_type)

                       }
                   }
            }

        }

document.addEventListener("click", click);