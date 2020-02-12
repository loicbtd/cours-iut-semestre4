function initialize_game(){

    // global vars
    theme = "unicorn"; // available: unicorn
    card_size = 100;
    grid_size_x = 8;
    grid_size_y = 8;
    number_of_cards = 8;
    number_of_cards_to_align = 3;
    model = Array();

    // dom elements
    element_container_header = document.getElementById("container-header");
    element_container_grid = document.getElementById("container-grid");
    element_container_progressbar = document.getElementById("container-progressbar");

    // set event listeners
    document.getElementById("button-high-scores").addEventListener("click", display_high_scores);
    document.getElementById("button-new-game").addEventListener("click", start_game);

    // set style
    document.getElementsByTagName("body")[0].style.backgroundImage = "url('resources/themes/"+theme+"/background.png')";

    start_game();
}

function start_game(){
    new_model();
    new_grid();
    update_grid();
}

function remove_good_cards(){
    // const
    // let number_of_removed_cards = 0;
    //
    // for (let y = 0; y < x; y++) {
    //
    // }
}

function new_model(){
    model = Array();
    let line_tmp;
    for (let y = 0; y < grid_size_y; y++) {
        line_tmp = Array();
        for (let x = 0; x < grid_size_x; x++) {
            line_tmp.push((Math.random() * (number_of_cards - 1) + 1).toFixed(0));
        }
        model.push(line_tmp);
    }
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
            document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img draggable='false' src='resources/themes/"+theme+"/cards/"+model[y][x]+".png' width='"+card_size+"' height='"+card_size*(5/6)+"'>";
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