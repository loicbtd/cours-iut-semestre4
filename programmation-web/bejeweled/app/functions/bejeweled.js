function initialize_game(){

    // dom elements
    element_container_header = document.getElementById("container-header");
    element_container_grid = document.getElementById("container-grid");
    element_container_progressbar = document.getElementById("container-progressbar");

    // set event listeners
    document.getElementById("button-high-scores").addEventListener("click", display_high_scores);
    document.getElementById("button-new-game").addEventListener("click", start_game);

    // global vars
    grid_size_x = 8;
    grid_size_y = 8;
    model = Array();
    
    start_game();
}

function start_game(){
    new_model();
    new_grid();
    update_grid();
}

function new_model(){
    model = Array();
    let line_tmp;
    for (let y = 0; y < grid_size_y; y++) {
        line_tmp = Array();
        for (let x = 0; x < grid_size_x; x++) {
            line_tmp.push((Math.random() * (8 - 1) + 1).toFixed(0));
        }
        model.push(line_tmp);
    }
    
    let is_valid = false;
    
    do {
        for (let y = 0; y < model.length - 3; y++) {
            for (let x = 0; x < model[y].length - 3; x++) {
                
            }
        }
    } while(!is_valid);
}

function new_grid(){
    let element_table = "";
    let element_row = "";

    element_table += "<table>";
    for (let y = 0; y < grid_size_y; y++) {
        element_row = "<tr class='table-row' id='table-row-"+y+"'>";
        for (let x = 0; x < grid_size_x; x++) {
            element_row += "<td class='cell' id='cell-row-"+y+"-col-"+x+"'></td>"
        }
        element_row += "</tr>";
        element_table += element_row;
    }
    element_table += "</table>";
    element_container_grid.innerHTML = element_table;
}

function update_grid() {

    for (let y = 0; y < model.length; y++) {
        for (let x = 0; x < model[y].length; x++) {
            document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img draggable='false' src='resources/images/gemstone-"+model[y][x]+".png' width='60' height='50'>";
        }
    }
    // for (let y = 0; y < grid_size_y; y++) {
    //     for (let x = 0; x < grid_size_x; x++) {
    //         let cell = ;
    //         let i = (Math.random() * (8 - 1) + 1).toFixed(0);
    //     }
    // }
}

function display_high_scores(){
}