function initialize_game(){

    // global vars
    theme = "tron"; // available: unicorn
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
    document.getElementById("button-pause").addEventListener("click", pause_unpause_game);
    document.getElementById("button-hint").addEventListener("click", handle_hint);

    // set style
    document.getElementsByTagName("body")[0].style.backgroundImage = "url('resources/themes/"+theme+"/background.png')";

    start_game();
}

function start_game(){
    level = 0;
    timer = 1;
    score = 0;
    tries_left = 5;
    majoration_coefficient = 0;

    isPaused = false;
    clock = setInterval( function (){
        if (!isPaused) {
            change_timer_value(-1 - level/10 );
        }
    }, 3000);

    new_model();
    new_grid();
    update_grid();
    update_game_informations();
    add_event_listener_on_grid();
}

function tag_cards_in_good_sequences(good_sequences_card_coordinates){
    let x;
    let y;
    for (let i = 0; i < good_sequences_card_coordinates.length - 1; i+=2) {
        y = good_sequences_card_coordinates[i] - 1;
        x = good_sequences_card_coordinates[i+1] - 1;
        model[y][x] = null_value;
    }
}

function get_coordinates_of_cards_in_good_sequence(){

    let coordinates_of_cards_in_good_sequence = Array();
    let coordinates_of_cards;
    let previous_card_value;
    let current_card_value;
    let position;
    let loop_condition;

    for (let y = 0; y < grid_size_y; y++) {
        for (let x = 0; x < grid_size_x; x++) {
            // if the current position allows to find good sequences before the end of the row
            if (x + number_of_cards_to_align - 1 < grid_size_x) {
                coordinates_of_cards = Array();
                position = 0;
                // manually do one loop iteration to initialize previous card value
                coordinates_of_cards.push(y+1);
                coordinates_of_cards.push(x+position+1);
                previous_card_value = model[y][x+position];
                position ++;

                // while we are sure to not overstep the end of the grid
                loop_condition = true;
                while (loop_condition && x + position < grid_size_x){
                    current_card_value = model[y][x+position]; // set the current card value
                    // if all the values in the sequence are equals the continue, else stop loop. (NB:  For [A, B, C], if A=B and B=C then A=B=C)
                    if(current_card_value === previous_card_value) {
                        coordinates_of_cards.push(y+1); // add the coordinate [y, x] to the list of coordinates
                        coordinates_of_cards.push(x+position+1); // add the coordinate [y, x] to the list of coordinates
                        previous_card_value = current_card_value; // set the previous card value for the next loop iteration
                        position++; // increment position for the next loop iteration
                    }
                    else {
                        loop_condition = false;
                    }
                }
                // console.log(coordinates_of_cards);
                // At the end of the loop, if the length of memorized coordinates is equal or higher than number_of_cards_to_align add them to
                // console.log("coordinates_of_cards.length: " + coordinates_of_cards.length / 2);
                if (coordinates_of_cards.length / 2 >= number_of_cards_to_align){
                    coordinates_of_cards_in_good_sequence = coordinates_of_cards_in_good_sequence.concat(coordinates_of_cards);
                }
            }
            // if the current position allows to find good sequences before the end of the column
            if (y + number_of_cards_to_align - 1 < grid_size_y){
                coordinates_of_cards = Array();
                position = 0;
                // manually do one loop iteration to initialize previous card value
                coordinates_of_cards.push(y+position+1);
                coordinates_of_cards.push(x+1);
                previous_card_value = model[y+position][x];
                position ++;
                // while we are sure to not overstep the end of the grid
                loop_condition = true;
                while (loop_condition && y + position < grid_size_y){
                    current_card_value = model[y+position][x]; // set the current card value
                    // if all the values in the sequence are equals the continue, else stop loop. (NB:  For [A, B, C], if A=B and B=C then A=B=C)
                    if(current_card_value === previous_card_value) {
                        coordinates_of_cards.push(y+position+1); // add the coordinate [y, x] to the list of coordinates
                        coordinates_of_cards.push(x+1); // add the coordinate [y, x] to the list of coordinates
                        previous_card_value = current_card_value; // set the previous card value for the next loop iteration
                        position++; // increment position for the next loop iteration
                    }
                    else {
                        loop_condition = false;
                    }
                }
                // At the end of the loop, if the length of memorized coordinates is equal or higher than number_of_cards_to_align add them to
                if (coordinates_of_cards.length / 2 >= number_of_cards_to_align){
                    coordinates_of_cards_in_good_sequence = coordinates_of_cards_in_good_sequence.concat(coordinates_of_cards);
                }
            }
        }
    }
    return coordinates_of_cards_in_good_sequence;
}

function drop_cards(){
    for (let y = model.length - 1; y > 0 ; y--) {
        for (let x = 0; x < model[y].length; x++) {
            if (model[y][x] === null_value){
                model[y][x] = model[y-1][x];
                model[y-1][x] = null_value;
            }
        }
        update_grid();
    }
}

function fill_null_cards(){
    for (let y = 0; y < model.length ; y++) {
        for (let x = 0; x < model[y].length; x++) {
            if (model[y][x] === null_value){
                model[y][x] = (Math.random() * (number_of_cards - 1) + 1).toFixed(0);
            }
        }
    }
    update_grid();
}

function new_model(){
    do {
        model = Array();
        let line_tmp;
        for (let y = 0; y < grid_size_y; y++) {
            line_tmp = Array();
            for (let x = 0; x < grid_size_x; x++) {
                line_tmp.push((Math.random() * (number_of_cards - 1) + 1).toFixed(0));
            }
            model.push(line_tmp);
        }
    } while (get_coordinates_of_cards_in_good_sequence().length !== 0);
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
              document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img class='disable-select' src='resources/themes/"+theme+"/cards/"+model[y][x]+".png' alt='"+model[y][x]+"'>";
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

function remove_event_listener_on_grid() {
    for (let y = 0; y < model.length; y++) {
        for (let x = 0; x < model[y].length; x++) {
            document.getElementById("cell-row-"+y+"-col-"+x).removeEventListener("click", permute_cards);
        }
    }
}

function permute_cards(event){
    if (first_card === null){
        first_card = event.target.id;
        return;
    }
    second_card = event.target.id;

    let first_card_y = parseInt(first_card.match(/\d/g)[0]);
    let first_card_x = parseInt(first_card.match(/\d/g)[1]);

    let second_card_y = parseInt(second_card.match(/\d/g)[0]);
    let second_card_x = parseInt(second_card.match(/\d/g)[1]);
    first_card = null;
    second_card = null;

    // if the two selected cards
    if (second_card_x > first_card_x + 1 || second_card_x < first_card_x - 1 ||
        second_card_y > first_card_y + 1 || second_card_y < first_card_y - 1) {
        alert("You must select two cards next to each other.");
        return;
    }

    let first_card_value = model[first_card_y][first_card_x];
    let second_card_value = model[second_card_y][second_card_x];

    let saved_model = model;
    model[first_card_y][first_card_x] = second_card_value;
    model[second_card_y][second_card_x] = first_card_value;

    let good_sequences_card_coordinates = get_coordinates_of_cards_in_good_sequence();

    if (good_sequences_card_coordinates.length === 0){
        model = saved_model;
        tries_left--;
        update_game_informations();
    }
    else {
        tag_cards_in_good_sequences(good_sequences_card_coordinates);
        drop_cards();
        fill_null_cards();
        handle_good_permutation(good_sequences_card_coordinates.length / 2);

        do {
            good_sequences_card_coordinates = get_coordinates_of_cards_in_good_sequence();
            tag_cards_in_good_sequences(good_sequences_card_coordinates);
            drop_cards();
            fill_null_cards();
            handle_good_permutation(good_sequences_card_coordinates.length / 2);
        } while (good_sequences_card_coordinates.length !== 0);
    }
}

function handle_good_permutation(number_of_good_cards){
    timer += 10;
    update_game_informations();

    if (number_of_good_cards >= number_of_cards_to_align + 2) {
        score += 1000 + 1000 * (level/10);
    }
    else if (number_of_good_cards === number_of_cards_to_align + 1) {
        score += 300 + 300 * (level/10);
    }
    else if (number_of_good_cards === number_of_cards_to_align) {
        score += 100 + 100 * (level/10);
    }
    update_game_informations();
}

function pause_unpause_game(){
    if (isPaused) {
        isPaused = false;
        document.getElementById("button-pause").innerHTML = '<i class="fas fa-pause"></i> Pause</i>';
        add_event_listener_on_grid();
    }
    else {
        isPaused = true;
        document.getElementById("button-pause").innerHTML = '<i class="fas fa-play"></i> Play';
        remove_event_listener_on_grid();
    }
}

function change_timer_value(difference) {
    timer += difference;

    if (timer <= 0 || tries_left <= 0){
        alert("Game Over !");
        pause_unpause_game();
    }

    if (timer >= 100) {
        level++;
        timer = timer - 100;
    }
    update_game_informations();
}

function update_game_informations(){
    document.getElementById("tries-left-value").innerHTML = tries_left;
    document.getElementById("score-value").innerHTML = score;
    document.getElementById("progressbar").value = timer;
}

function display_high_scores(){
    alert("High scores");
}

function handle_hint() {
    alert("hint");
}