
//function test(data){
//console.log(data)
////alert("Page is loaded");
////let el = document.getElementById ("t");
////el.style.innerHTML = p;
//}

function draw_player_misses(coordinates){
 /**
* draws player's misses on an opponent's board by coloring it white
* @param coordinates arg1 coordinates{x,y} of a miss to draw
*/
 let element = document.getElementById (`o${coordinates.x}${coordinates.y}`);
    element.style.backgroundColor = 'white';
}


function draw_opponent_misses(coordinates){
 /**
* draws opponents's misses on an players's board by coloring it white
* @param coordinates arg1 coordinates{x,y} of a miss to draw
*/
 let element = document.getElementById (`y${coordinates.x}${coordinates.y}`);
    element.style.backgroundColor = 'white';
}

//
function draw_ship(coordinates){
 /**
* draw player's ships by coloring it light blue
* @param coordinates arg1 coordinates{x,y} of a miss to draw
*/
    let element = document.getElementById (`y${coordinates.x}${coordinates.y}`);
    element.style.visibility = 'visible';
    element.style.backgroundColor = "lightblue";
}

//
function draw_hit_to_player_ships(coordinates){
 /**
* draw hits to player's ships by coloring it red
* @param coordinates arg1 coordinates{x,y} of a miss to draw
*/
    let element = document.getElementById (`y${coordinates.x}${coordinates.y}`);
    element.style.visibility = 'visible';
    element.style.backgroundColor = "red";
    }

function draw_hit_to_opponent_ships(coordinates){
 /**
* draw hits to opponent's ships by coloring it red
* @param coordinates arg1 coordinates{x,y} of a miss to draw
*/
    let element = document.getElementById (`o${coordinates.x}${coordinates.y}`);
    element.style.visibility = 'visible';
    element.style.backgroundColor = "red";
    }

//function hide_squeare(coordinates){
// /**
//* draw hits to opponent's ships by coloring it red
//* @param coordinates arg1 coordinates{x,y} of a miss to draw
//*/
//    let element = document.getElementById (coordinates);
//    element.style.visibility = 'hidden';
//}


// event handling
function click(event)
            {
                id = event.target.id
                if (id!= null && id.match(/^y[a-j]([123456789]|10)$/)!=null){
//                    game.guess(event.target.id);
//                      console.log(id)
                }

                if (id!= null && id.match(/^o[a-j](10)$/)!=null){
                      window.location.href = "/status"+id[1]+'10';
//                      console.log(event.target.id)
                }

                else if (id!= null && id.match(/^o[a-j][0123456789]$/)!=null){
                    window.location.href = "/status"+id[1]+id[2];
//                      console.log(event.target.id)
                }

            }
document.addEventListener("click", click);
