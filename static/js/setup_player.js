class Setup {
  constructor() {
  let shipType = 0;
let shipCellsSet = 0;
let shipSet = [4,3,3,2,2,2,1];
let lastClickedCellId = null;
let name_is_set = false;
let ships_are_set = false;
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


function set_name(player){
name = document.getElementById("name").value;
var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        stBtn = document.getElementById("confirmBtn");
        stBtn.style.cursor= "not-allowed";
        stBtn.style.pointerEvents= "none";
        console.log("player "+ player +" name " + name)
      }
      }
    xhttp.open("GET", "/set_name/"+player+"/"+name, true);
    xhttp.send();
}

function isNeighbourCell(cell_id, lastChecked){
    if (lastChecked == null)
        return true;

    let letters = ['a','b','c','d','e','f','g','h','i','j'];
    let lastletterIndex = (letters.indexOf(lastChecked[1]));
    let thisletterIndex = (letters.indexOf(cell_id[1]));
    let thisNumberInt = parseInt(cell_id[2], 10);
    let lastNumberInt = parseInt(lastChecked[2], 10);
    console.log('li:'+lastletterIndex+'ci:'+thisletterIndex+ 'ln:'+lastNumberInt+'cn'+thisNumberInt)
    if ((lastletterIndex == thisletterIndex+1|| lastletterIndex == thisletterIndex-1)&lastNumberInt == thisNumberInt)
        return true;
    else if ((lastNumberInt == thisNumberInt+1|| lastNumberInt == thisNumberInt-1)&lastletterIndex == thisletterIndex)
        return true;
    else
        return false;
}


function renewBoard(){
    let letters = ['a','b','c','d','e','f','g','h','i','j'];

    for (let i=1; i<11; i++){
         for (let j=0; j<10; j++){

            element = document.getElementById('y'+letters[j]+[i])
            element.style.backgroundColor = 'lightgray';
            }
    }
}

function addShip(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        reNewShip();
        renewBoard();
        noneChecked();
      }
      }
    xhttp.open("GET", "/add_ship", true);
    xhttp.send();

}

function reNewShip(){
    setup.shipType = 0;
    setup.shipCellsSet = 0;
    setup.shipCellsSet = 0;
}

function click(event)
        {
            id = event.target.id;
            if (id!= null && id.match(/^t[1234]$/)!=null){
                element = document.getElementById(id);
                onlyOneChecked(element);

                setup.lastClickedCellId = null;
                reNewShip();
                renewBoard();

                setup.shipType = id[1];

                setup.shipCellsSet = 0;
                console.log(setup.shipType);
            }

            else if (id!= null && id.match(/(^y[a-j](10)$)|(^y[a-j][0123456789]$)/)!=null){
                   console.log(isNeighbourCell(id, setup.lastClickedCellId));
                   if (isNeighbourCell(id, setup.lastClickedCellId)){
                       setup.lastClickedCellId = id;
                       setup.shipCellsSet ++;
                       element = document.getElementById(id);
                       if(setup.shipCellsSet<=setup.shipType){
                           element.style.backgroundColor = 'gray';
                       }
                   }
            }

        }

document.addEventListener("click", click);