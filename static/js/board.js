console.log("hello world")

function test(data){
console.log(data)
//alert("Page is loaded");
//let el = document.getElementById ("t");
//el.style.innerHTML = p;
}

function draw_player_misses(coordinates){
 let element = document.getElementById (`o${coordinates.x}${coordinates.y}`);
    console.log("hide"+`o${coordinates.x}${coordinates.y}`);
    // element.style.visibility = 'hidden';
    element.style.backgroundColor = 'white';
    return element;
}

function draw_opponent_misses(coordinates){
 let element = document.getElementById (`y${coordinates.x}${coordinates.y}`);
    console.log("hide"+`y${coordinates.x}${coordinates.y}`);
    element.style.backgroundColor = 'white';
    return element;
}


function draw_ship(coordinates){
    let element = document.getElementById (`y${coordinates.x}${coordinates.y}`);
    console.log(`y${coordinates.x}${coordinates.y}`);
    // element.style.backgroundColor = "black"
//    element.style.fill = 'rgb(0,0,204)';
    element.style.visibility = 'visible';
    element.style.backgroundColor = "lightblue";
    return element;
}

function hide_squeare(coordinates){
    let element = document.getElementById (coordinates);
    element.style.visibility = 'hidden';
    return element;
}


// event handling
function click(event)
            {
                id = event.target.id
                if (id!= null && id.match(/^y[a-j]([123456789]|10)$/)!=null){
//                    game.guess(event.target.id);
                      console.log(id)
                }

                if (id!= null && id.match(/^o[a-j](10)$/)!=null){
                      window.location.href = "/status"+id[1]+'10';
                      console.log(event.target.id)
                }

                else if (id!= null && id.match(/^o[a-j][0123456789]$/)!=null){
                    window.location.href = "/status"+id[1]+id[2];
                      console.log(event.target.id)
                }

            }
document.addEventListener("click", click);
