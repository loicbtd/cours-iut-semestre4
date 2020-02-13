function initialize_game(){

    // global vars
    theme = "unicorn"; // available: unicorn
    card_size = 100;
    grid_size_x = 8;
    grid_size_y = 8;
    number_of_cards = 8;
    number_of_cards_to_align = 3;
    null_value = -1;
    model = Array();
    first_card = null;
    second_card = null;

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
    add_event_listener_on_grid();
}

function remove_good_sequences(){
    let comparaisonList;

    for (let y = 0; y < grid_size_y; y++) {
        for (let x = 0; x < grid_size_x; x++) {
            if (x + number_of_cards_to_align <= grid_size_x ){
                // test if row is good
                comparaisonList = Array();
                for (let pos = 0; pos < number_of_cards_to_align; pos++) {
                    comparaisonList.push(model[y][x+pos]);
                }
                // if row is good put null_value on it
                if (comparaisonList.every( (val, i, arr) => val === arr[0] )){
                    for (let pos = 0; pos < number_of_cards_to_align; pos++) {
                        model[y][x+pos] = null_value;
                    }
                }
            }
            if (y + number_of_cards_to_align <= grid_size_y){
                // test if column is good
                comparaisonList = Array();
                for (let pos = 0; pos < number_of_cards_to_align; pos++) {
                    comparaisonList.push(model[y+pos][x]);
                }
                // if column is good put null_value on it
                if (comparaisonList.every( (val, i, arr) => val === arr[0] )){
                    for (let pos = 0; pos < number_of_cards_to_align; pos++) {
                        model[y+pos][x] = null_value;
                    }
                }
            }
        }
    }
}

function test_good_sequences(){
    let number_of_good_sequences = 0;
    let comparaisonList;

    for (let y = 0; y < grid_size_y; y++) {
        for (let x = 0; x < grid_size_x; x++) {
            if (x + number_of_cards_to_align <= grid_size_x ) {
                // test if row is good
                comparaisonList = Array();
                for (let pos = 0; pos < number_of_cards_to_align; pos++) {
                    comparaisonList.push(model[y][x+pos]);
                }
                // if row is good put null_value on it
                if (comparaisonList.every( (val, i, arr) => val === arr[0] )){
                    number_of_good_sequences++;
                }
            }
                if (y + number_of_cards_to_align <= grid_size_y){
                // test if column is good
                comparaisonList = Array();
                for (let pos = 0; pos < number_of_cards_to_align; pos++) {
                    comparaisonList.push(model[y+pos][x]);
                }
                // if column is good put null_value on it
                if (comparaisonList.every( (val, i, arr) => val === arr[0] )){
                    number_of_good_sequences++;
                }
            }
        }
    }
    return number_of_good_sequences;
}

function fill_empty_cells(){
    for (let y = 0; y < model.length; y++) {
        for (let x = 0; x < model[y].length; x++) {
            if (model[y][x] === -1){
                model[y][x] = (Math.random() * (number_of_cards - 1) + 1).toFixed(0);
            }
        }
    }
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

    while (test_good_sequences() !== 0){
        remove_good_sequences();
        fill_empty_cells();
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
            document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img class='disable-select' src='resources/themes/"+theme+"/cards/"+model[y][x]+".png' width='"+card_size+"' height='"+card_size*(5/6)+"'>";
        }
    }
}

function add_event_listener_on_grid(){
    for (let y = 0; y < model.length; y++) {
        for (let x = 0; x < model[y].length; x++) {
            document.getElementById("cell-row-"+y+"-col-"+x).addEventListener("click", permute_cards);
        }
    }
}

function permute_cards(card){
    if (first_card === null){
        first_card = card.target.id;
        return;
    }
    second_card = card.target.id;

    let first_card_x = parseInt(first_card.match(/\d/g)[0]);
    let first_card_y = parseInt(first_card.match(/\d/g)[1]);

    let second_card_x = parseInt(second_card.match(/\d/g)[0]);
    let second_card_y = parseInt(second_card.match(/\d/g)[1]);

    let first_card_value = parseInt(model[first_card_x][first_card_y]);
    let second_card_value = parseInt(model[second_card_x][second_card_y]);

    if (first_card_value !== second_card_value){
        model[first_card_x][first_card_y] = second_card_value;
        model[second_card_x][second_card_y] = first_card_value;
    }

    // console.log(" first card | " + first_card + " | row: " + first_card.match(/\d/g)[0] + " | col: " + first_card.match(/\d/g)[1]);
    // console.log( " second card | " + second_card + " | row: " + second_card.match(/\d/g)[0] + " | col: " + second_card.match(/\d/g)[1]);

    update_grid();


    first_card = null;
    second_card = null;
}

function display_high_scores(){
}