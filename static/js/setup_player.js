class Setup {
  constructor() {
    this.current_ship = null;
    this.selection = new Selection();
    this.list_of_ships = [];
    this.player = null;
    // this.shipSet = getRules();//number of elements: number of ships, values: types of ships
    this.ship_stack = [1,2];
//
//    let name_is_set = false;
//    let ships_are_set = false;
}

  remove_from_stack(ship){
    /**
    * Removes a placed ship by ship type (size of the ship)
    * @param ship arg1 a ship object
    */
    let index = this.ship_stack.indexOf(parseInt(ship.s_type, 10));
    if (index > -1) {
        this.ship_stack.splice(index, 1);
    }
  }


//
//    reNewShip(){
//        setup.shipType = 0;
//        setup.shipCellsSet = 0;
//        setup.shipCellsSet = 0;
//    }

//    FIXME
    is_too_close_to_another_ship(coordinates){
    /**
     * Check if current coordinates are next to another ship
     * @param  coordinates arg1 coordinates on the board
     */
        for (let i = 0; i<this.list_of_ships.length; i++){
            let ship_obj = this.list_of_ships[i];
            for (let j = 0; j<ship_obj.set_of_coordinates.length; j++){
                let coordinates_obj = ship_obj.set_of_coordinates[j];
                if (coordinates.is_neighbour_coordinates(coordinates_obj))
                    return true;
            }
        }
        return false;
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

    is_neighbour_coordinates(coordinates_lee){
    /**
    * compares two coordinates and decides if they are close to each other
    * including diagonal neighbourhood
    */
        let letters = ['a','b','c','d','e','f','g','h','i','j'];
        let foo_letter_index = letters.indexOf(this.x);
        let lee_letter_index = letters.indexOf(coordinates_lee.x);
        if ((foo_letter_index == lee_letter_index+1 | foo_letter_index == lee_letter_index-1 | foo_letter_index == lee_letter_index) &
            (this.y == coordinates_lee.y +1 | this.y == coordinates_lee.y-1 | this.y == coordinates_lee.y))
            {
            return true;
            }
        else if (this.x == coordinates_lee.y & this.x == coordinates_lee.y){
            return true;
            }

        else{
            return false;
        }
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

    is_allowed(id, number_of_selected_cells, lastClickedCellId) {
         if ((number_of_selected_cells<this.s_type)&is_neighbour_cell(id ,lastClickedCellId)){
                return true;
        }
        else
        return false;
    }

    is_fully_located(num){
    /**
    * This function decides if a ship has been completely put to the table
    */
        if (num == this.s_type & this.s_type!=0)
            return true;
        else
           return false;
    }
}

setup = new Setup();



function onlyOneChecked(checkbox) {
    /**
     * Allows only one of checkboxes at a time to be toggled
     * @param  checkbox arg1 checkbox document element
     */
    var checkboxes = document.getElementsByName('check');
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

function checkboxes_check(list_of_types){
var checkboxes = document.getElementsByName('check');
    checkboxes.forEach((checkbox) => {
    if (list_of_types.indexOf(parseInt(checkbox.id[1], 10)) == -1)
        checkbox.disabled = true;
    });
}


function is_neighbour_cell(cell_id, lastChecked){
/**
*Compares two id of elements and decides if the elements are neighbours on the board. Excluding diagonal neighborhood
*@param cell_id arg1 id of a cell
*@param lastChecked arg2 id of last clicked cell
*/
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
    * erases only gray squares
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
    /**
    * Adds ship to setup's list of ship to be sent to the model
    */

    setup.list_of_ships.push(ship_obj);
    setup.remove_from_stack(ship_obj);
    checkboxes_check(setup.ship_stack);

    ship_obj.set_of_coordinates.forEach((item) => {
        element= document.getElementById("y"+item.x+item.y);
        element.style.backgroundColor = 'skyblue';
    });

        setup.current_ship = new Ship(0);
//        reNewShip();
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
        let buttons = document.getElementsByName('next');
        buttons.forEach((button) => {
        console.log(button);
        button.disabled = false;
        button.className = "next-button";
        });
      }
      }
    var data = JSON.stringify(setup_obj);

    xhttp.open("POST", "/save_setup/"+player, true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    console.log(setup.current_ship)
    xhttp.send(data);

}


function process_ship_type_checkbox_click(element){
    renewBoard(); // renew board
    setup.selection = new Selection();

     if (element.checked==true){
        onlyOneChecked(element);
//        reNewShip(); //renews visual atributes of a ship
        setup.current_ship = new Ship(id[1]);

     }
     else{// unchecked
        setup.current_ship = new Ship(0);
     }
}

function process_board_cell_click_event(element){
    if (setup.current_ship.is_allowed(id, setup.selection.number_of_selected_cells,
    setup.selection.lastClickedCellId, setup.set_of_types) & (!setup.is_too_close_to_another_ship(new Coordinates(id[1],
    parseInt(id.substring(2), 10)), setup))){

       setup.selection.lastClickedCellId = id;
       setup.selection.number_of_selected_cells++;
       element.style.backgroundColor = 'gray';
       setup.current_ship.add_coordinates(new Coordinates(id[1], parseInt(id.substring(2), 10)));
    }

   if (setup.current_ship.is_fully_located(setup.selection.number_of_selected_cells)){
        btn = document.getElementById("confirmShipBtn");
        btn.disabled=false;
        btn.className = "confirm-button";
        }
}



function click(event){
    /**
    *Handles clicks on different elements of UI
    *@param event - event click
    */

    id = event.target.id;
    element = document.getElementById(id);
    //if toggled/untogled checkbox
    if (id!= null && id.match(/^t[1234]$/)!=null)
        process_ship_type_checkbox_click(element);

    //if a cell on the board is clicked
    else if (id!= null && id.match(/(^y[a-j](10)$)|(^y[a-j][0123456789]$)/)!=null)
        process_board_cell_click_event(element);

}
checkboxes_check(setup.ship_stack);
document.addEventListener("click", click);
