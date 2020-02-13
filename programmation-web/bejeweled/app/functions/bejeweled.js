function initialize_game(){

    // global vars
    theme = "tron"; // available: unicorn
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

function get_coordinates_of_cards_in_good_sequence(){

    let coordinates_of_cards_in_good_sequence = Array();
    let coordinates_of_cards;
    let previous_card_value;
    let current_card_value;
    let position;

    for (let y = 0; y < grid_size_y; y++) {
        for (let x = 0; x < grid_size_x; x++) {
            // if the current position allows to find good sequences before the end of the row
            if (x + number_of_cards_to_align < grid_size_x + 1) {
                coordinates_of_cards = Array();
                position = 0;
                // manually do one loop iteration to initialize previous card value
                coordinates_of_cards.push([y][x+position]);
                previous_card_value = model[y][x+position];
                position ++;
                // while we are sure to not overstep the end of the grid
                while (position + x + number_of_cards_to_align < grid_size_x + 1){
                    current_card_value = model[y][x+position]; // set the current card value
                    if(current_card_value !== previous_card_value) break; // if all the values in the sequence are equals the continue, else stop loop. (NB:  For [A, B, C], if A=B and B=C then A=B=C)
                    coordinates_of_cards.push([y][x+position]); // add the coordinate [y, x] to the list of coordinates
                    previous_card_value = current_card_value; // set the previous card value for the next loop iteration
                    position++; // increment position for the next loop iteration
                }
                // At the end of the loop, if the length of memorized coordinates is equal or higher than number_of_cards_to_align add them to
                if (coordinates_of_cards.length >= number_of_cards_to_align){
                    coordinates_of_cards_in_good_sequence.concat(coordinates_of_cards);
                }
            }
            // if the current position allows to find good sequences before the end of the column
            if (y + number_of_cards_to_align < grid_size_y + 1){
                coordinates_of_cards = Array();
                position = 0;
                // manually do one loop iteration to initialize previous card value
                coordinates_of_cards.push([y+position][x]);
                previous_card_value = model[y+position][x];
                position ++;
                // while we are sure to not overstep the end of the grid
                while (position + y + number_of_cards_to_align < grid_size_y + 1){
                    current_card_value = model[y+position][x]; // set the current card value
                    if(current_card_value !== previous_card_value) break; // if all the values in the sequence are equals the continue, else stop loop. (NB:  For [A, B, C], if A=B and B=C then A=B=C)
                    coordinates_of_cards.push([y+position][x]); // add the coordinate [y, x] to the list of coordinates
                    previous_card_value = current_card_value; // set the previous card value for the next loop iteration
                    position++; // increment position for the next loop iteration
                }
                // At the end of the loop, if the length of memorized coordinates is equal or higher than number_of_cards_to_align add them to
                if (coordinates_of_cards.length >= number_of_cards_to_align){
                    coordinates_of_cards_in_good_sequence.concat(coordinates_of_cards);
                }
            }
        }
    }
    return coordinates_of_cards_in_good_sequence;
}

function fill_empty_cells(){
    for (let y = 0; y < model.length; y++) {
        for (let x = 0; x < model[y].length; x++) {
            if (model[y][x] === -1){
                let new_value;
                do {
                    new_value = (Math.random() * (number_of_cards - 1) + 1).toFixed(0);
                } while (new_value === model[y][x]);
                model[y][x] = new_value;
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

    while (get_coordinates_of_cards_in_good_sequence().length !== 0){
        remove_good_sequences();
        fill_empty_cells();
    }
}

function new_grid(){
    let element_table = "";
    let element_row = "";

    element_table += "<table class='col-100'>";
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
            // document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img class='disable-select' src='resources/themes/"+theme+"/cards/"+model[y][x]+".png' width='"+card_size+"' height='"+card_size*(5/6)+"'>";
            document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img class='disable-select' src='resources/themes/"+theme+"/cards/"+model[y][x]+".png'>";
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

function permute_cards(event){
    if (first_card === null){
        first_card = event.target.id;
        return;
    }
    second_card = event.target.id;

    let first_card_x = parseInt(first_card.match(/\d/g)[0]);
    let first_card_y = parseInt(first_card.match(/\d/g)[1]);

    let second_card_x = parseInt(second_card.match(/\d/g)[0]);
    let second_card_y = parseInt(second_card.match(/\d/g)[1]);

    let first_card_value = parseInt(model[first_card_x][first_card_y]);
    let second_card_value = parseInt(model[second_card_x][second_card_y]);

    let saved_model = model;
    model[first_card_x][first_card_y] = second_card_value;
    model[second_card_x][second_card_y] = first_card_value;

    if (get_coordinates_of_cards_in_good_sequence() === 0){
        model = saved_model;
    }

    remove_good_sequences();
    fill_empty_cells();
    update_grid();

    // console.log(" first card | " + first_card + " | row: " + first_card.match(/\d/g)[0] + " | col: " + first_card.match(/\d/g)[1]);
    // console.log( " second card | " + second_card + " | row: " + second_card.match(/\d/g)[0] + " | col: " + second_card.match(/\d/g)[1]);

    first_card = null;
    second_card = null;
}

function display_high_scores(){
}

/*
1. remplir tableau sans bonne sequences

2. mouvement

3. test



 */