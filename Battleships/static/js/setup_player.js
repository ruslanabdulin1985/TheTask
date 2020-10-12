// Goes together with setup_player_model.js
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
   /**
     * Disables all the checkboxes for ships not in ship_stock so they couldn't be placed on a board
     * @param list_of_types arg1 list ship types in stock
     */
var checkboxes = document.getElementsByName('check');
    checkboxes.forEach((checkbox) => {
    if (list_of_types.indexOf(parseInt(checkbox.id[1], 10)) == -1)
        checkbox.disabled = true;
    });
}

function draw_examples(){
    /**
     * Shows an example how to place a ship on a board
     *
     */
   checkboxes= document.getElementsByName('check');
     checkboxes.forEach((checkbox) => {
        if (checkbox.checked == true){
            number_of_cells = parseInt(checkbox.id[1],10);
//            console.log("c "+number_of_cells)
            html = "<div>Example:</div> <table>";
            for (let i=0; i<number_of_cells; i++){
                html += "<tr><td class='cell' style='background-color:lightblue'></td></tr>";
            }

            html += "</table>"
            document.getElementById("example1").innerHTML=html;
        }
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
    let thisNumberInt;
    let lastNumberInt;
    if (cell_id.length>3)
        thisNumberInt = 10;
    else
         thisNumberInt = parseInt(cell_id[2], 10);

    if (lastChecked.length>3)
         lastNumberInt = 10;
    else
         lastNumberInt = parseInt(lastChecked[2], 10);


    if ((lastletterIndex == thisletterIndex+1|| lastletterIndex == thisletterIndex-1)&lastNumberInt == thisNumberInt)
        return true;

    else if ((lastNumberInt == thisNumberInt+1|| lastNumberInt == thisNumberInt-1)&lastletterIndex == thisletterIndex)
        return true;
    else
        return false;
}


function renewBoard(){
    /**
    * Clean the board selection marked for a new ship
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
    update_stock_ship_counters();


    ship_obj.set_of_coordinates.forEach((item) => {
        element= document.getElementById("y"+item.x+item.y);
        element.style.backgroundColor = 'skyblue';
    });

        setup.current_ship = new Ship(0);
        renewBoard();
        noneChecked();
        btn = document.getElementById("confirmShipBtn");
        btn.disabled=true;
        btn.className = "inactive-button";
}

function save_setup(player, setup_obj){
     /**
    * Sends the setup to the model
    */

    setup.player = new Player(document.getElementById('name').value);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {

      if (this.readyState == 4 && this.status == 200) {
        let buttons = document.getElementsByName('next');
        buttons.forEach((button) => {
            button.className = 'next-button';
            button.disabled = false;
        });
      }
      }
    var data = JSON.stringify(setup_obj);

    xhttp.open("POST", "/save_setup/"+player, true);
    xhttp.setRequestHeader("Content-Type", "application/json");

//    console.log(setup.current_ship)
    xhttp.send(data);

}


function process_ship_type_checkbox_click(element){
/**
* execute actions when a check box element is clicked
* param element arg1 clicked element
*/
    renewBoard(); // renew board
    setup.selection = new Selection();

     if (element.checked==true){
        onlyOneChecked(element);
        setup.current_ship = new Ship(id[1]);

     }
     else{// unchecked
        setup.current_ship = new Ship(0);
     }
     draw_examples();
}

function process_board_cell_click_event(element){
        /**
    * execute actions when a cell on the board is clicked
    * param element arg1 clicked element
    */
    if (setup.current_ship==null)
        return false;

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

function update_stock_ship_counters(){
    /**
    *Updates numbers of ships available for placement
    */
    document.getElementById('carrier_counter').innerHTML = 'x'+ setup.number_of(4);
    document.getElementById('battleship_counter').innerHTML = 'x'+ setup.number_of(3);
    document.getElementById('destroyer_counter').innerHTML = 'x'+ setup.number_of(2);
    document.getElementById('submarine_counter').innerHTML = 'x'+ setup.number_of(1);
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

setup = new Setup();
checkboxes_check(setup.ship_stack);
update_stock_ship_counters();
document.addEventListener("click", click);
