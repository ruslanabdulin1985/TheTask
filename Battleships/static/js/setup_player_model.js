class Setup {
/**
    * Setup represents a set of settings before a game starts
    *
    */
  constructor() {
   /**
    *
    * @param ship arg1 a ship object
    */
    this.current_ship = null;
    this.selection = new Selection();
    this.list_of_ships = [];
    this.player = null;
    console.log('tttt');

}

  get_rules(){
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

    xhttp.open("POST", "/save_setup/"+player, true);
    xhttp.setRequestHeader("Content-Type", "application/json");

    xhttp.send(data);

  }

  number_of(s_type){
  /**
  *Calculates and returns the number of ships of a certain type in stack to be placed
  *
  */
  let counter = 0;
   for (let i = 0; i< this.ship_stack.length; i++){
       if (this.ship_stack[i] == s_type){
        counter++;
       }
   }
   return counter;
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
    /*
    * Represents a view model of a player
    */
    constructor(name){
        this.name = name;
    }
}


class Selection{

 /*
    * Selection is a set of cells representing a ship to be placed
    */
constructor(){
         this.number_of_selected_cells = 0;
         this.lastClickedCellId = null;
    }
}

class Coordinates{
 /*
    * Coordinates on a board
    */
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
    /**
    * This function decides if a ship a selected cell is suitible to be a next part of the ship
    *
    *@param id arg1 id of an element to be placed
    *@param number_of_selected_cells arg2 how many sells are currently selected
    *@param lastClickedCellId arg3 id of the cell was previously clicked
    */
    if (lastClickedCellId == null)
        return true;

         if ((number_of_selected_cells<this.s_type)&is_neighbour_cell(id ,lastClickedCellId)){
                return true;
        }
        else
        return false;
    }

    is_fully_located(num){
    /**
    * This function decides if a ship has been completely put to the table
    * @param num arg1 number of currently clicked cells
    */
        if (num == this.s_type & this.s_type!=0)
            return true;
        else
           return false;
    }
}