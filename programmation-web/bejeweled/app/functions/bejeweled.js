

// view functions
function new_grid(){
    let element_table = "";
    let element_row = "";

    element_table += "<table class=''>";
    for (let y = 0; y < GRID_SIZE_Y; y++) {
        element_row = "<tr class='table-row' id='table-row-"+y+"'>";
        for (let x = 0; x < GRID_SIZE_X; x++) {
            element_row += "<td class='cell' id='cell-row-"+y+"-col-"+x+"'></td>"
        }
        element_row += "</tr>";
        element_table += element_row;
    }
    element_table += "</table>";
    ELEMENT_CONTAINER_GRID.innerHTML = element_table;
}

function update_grid() {
    for (let y = 0; y < global_model.length; y++) {
        for (let x = 0; x < global_model[y].length; x++) {
            document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img class='disable-select' src='resources/themes/"+THEME+"/cards/"+global_model[y][x]+".png' alt='"+global_model[y][x]+"'>";
        }
    }
}

function update_game_informations(){
    ELEMENT_TRIES_LEFT_VALUE.innerHTML = global_tries_left;
    ELEMENT_SCORE_VALUE.innerHTML = global_score;
    ELEMENT_PROGRESSBAR.value = global_timer;
}

function add_event_listener_on_grid(){
    for (let y = 0; y < global_model.length; y++) {
        for (let x = 0; x < global_model[y].length; x++) {
            document.getElementById("cell-row-"+y+"-col-"+x).addEventListener("click", handle_action_card_permutation);
        }
    }
}

function remove_event_listener_on_grid() {
    for (let y = 0; y < global_model.length; y++) {
        for (let x = 0; x < global_model[y].length; x++) {
            document.getElementById("cell-row-"+y+"-col-"+x).removeEventListener("click", handle_action_card_permutation);
        }
    }
}

function hide_grid(){
    for (let y = 0; y < global_model.length; y++) {
        for (let x = 0; x < global_model[y].length; x++) {
            document.getElementById("cell-row-"+y+"-col-"+x).innerHTML= "<img class='disable-select' hidden src='resources/themes/"+THEME+"/cards/"+global_model[y][x]+".png' alt='"+global_model[y][x]+"'>";
        }
    }
}

// model functions
function initialize_game(){

    // global constants
    THEME = "tron"; // available: unicorn
    GRID_SIZE_X = 8;
    GRID_SIZE_Y = 8;
    NUMBER_OF_CARDS = 8;
    NUMBER_OF_CARDS_TO_ALIGN = 3;
    NULL_VALUE = -1;

    // dom elements constants
    ELEMENT_CONTAINER_GRID = document.getElementById("container-grid");
    ELEMENT_TRIES_LEFT_VALUE = document.getElementById("tries-left-value");
    ELEMENT_SCORE_VALUE = document.getElementById("score-value");
    ELEMENT_PROGRESSBAR =  document.getElementById("progressbar");
    ELEMENT_BUTTON_PAUSE = document.getElementById("button-pause");
    ELEMENT_BUTTON_HIGH_SCORE = document.getElementById("button-high-scores");
    ELEMENT_BUTTON_NEW_GAME  = document.getElementById("button-new-game");
    ELEMENT_BUTTON_HINT = document.getElementById("button-hint");
    ELEMENT_BODY = document.getElementsByTagName("body")[0];


    // global vars
    global_model = Array();
    global_first_card = null;
    global_second_card = null;

    // set event listeners
    ELEMENT_BUTTON_HIGH_SCORE.addEventListener("click", handle_action_button_high_scores);
    ELEMENT_BUTTON_NEW_GAME.addEventListener("click", start_game);
    ELEMENT_BUTTON_PAUSE.addEventListener("click", handle_action_button_pause_unpause_game);
    ELEMENT_BUTTON_HINT.addEventListener("click", handle_action_button_hint);

    // set style
    ELEMENT_BODY.style.backgroundImage = "url('resources/themes/"+THEME+"/background.png')";

    get_data();

    start_game();
}

function start_game(){
    get_data();
    global_level = 0;
    global_timer = 1;
    global_score = 0;
    global_tries_left = 5;

    new_model();
    new_grid();
    update_grid();
    update_game_informations();

    global_is_paused = true;
    add_event_listener_on_grid();
    global_clock = setInterval( function (){
        if (!global_is_paused) {
            change_timer_value(-1 - global_level/10 );
        }
    }, 3000);
}

function new_model(){
    do {
        global_model = Array();
        let line_tmp;
        for (let y = 0; y < GRID_SIZE_Y; y++) {
            line_tmp = Array();
            for (let x = 0; x < GRID_SIZE_X; x++) {
                line_tmp.push((Math.random() * (NUMBER_OF_CARDS - 1) + 1).toFixed(0));
            }
            global_model.push(line_tmp);
        }
    } while (get_coordinates_of_cards_in_good_sequence().length !== 0);
}

function tag_cards_in_good_sequences(good_sequences_card_coordinates){
    let x;
    let y;
    for (let i = 0; i < good_sequences_card_coordinates.length - 1; i+=2) {
        y = good_sequences_card_coordinates[i] - 1;
        x = good_sequences_card_coordinates[i+1] - 1;
        global_model[y][x] = NULL_VALUE;
    }
}

function get_coordinates_of_cards_in_good_sequence(){

    let coordinates_of_cards_in_good_sequence = Array();
    let coordinates_of_cards;
    let previous_card_value;
    let current_card_value;
    let position;
    let loop_condition;

    for (let y = 0; y < GRID_SIZE_Y; y++) {
        for (let x = 0; x < GRID_SIZE_X; x++) {
            // if the current position allows to find good sequences before the end of the row
            if (x + NUMBER_OF_CARDS_TO_ALIGN - 1 < GRID_SIZE_X) {
                coordinates_of_cards = Array();
                position = 0;
                // manually do one loop iteration to initialize previous card value
                coordinates_of_cards.push(y+1);
                coordinates_of_cards.push(x+position+1);
                previous_card_value = global_model[y][x+position];
                position ++;

                // while we are sure to not overstep the end of the grid
                loop_condition = true;
                while (loop_condition && x + position < GRID_SIZE_X){
                    current_card_value = global_model[y][x+position]; // set the current card value
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
                if (coordinates_of_cards.length / 2 >= NUMBER_OF_CARDS_TO_ALIGN){
                    coordinates_of_cards_in_good_sequence = coordinates_of_cards_in_good_sequence.concat(coordinates_of_cards);
                }
            }
            // if the current position allows to find good sequences before the end of the column
            if (y + NUMBER_OF_CARDS_TO_ALIGN - 1 < GRID_SIZE_Y){
                coordinates_of_cards = Array();
                position = 0;
                // manually do one loop iteration to initialize previous card value
                coordinates_of_cards.push(y+position+1);
                coordinates_of_cards.push(x+1);
                previous_card_value = global_model[y+position][x];
                position ++;
                // while we are sure to not overstep the end of the grid
                loop_condition = true;
                while (loop_condition && y + position < GRID_SIZE_Y){
                    current_card_value = global_model[y+position][x]; // set the current card value
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
                if (coordinates_of_cards.length / 2 >= NUMBER_OF_CARDS_TO_ALIGN){
                    coordinates_of_cards_in_good_sequence = coordinates_of_cards_in_good_sequence.concat(coordinates_of_cards);
                }
            }
        }
    }
    return coordinates_of_cards_in_good_sequence;
}

function drop_cards(){
    for (let y = global_model.length - 1; y > 0 ; y--) {
        for (let x = 0; x < global_model[y].length; x++) {
            if (global_model[y][x] === NULL_VALUE){
                global_model[y][x] = global_model[y-1][x];
                global_model[y-1][x] = NULL_VALUE;
            }
        }
        update_grid();
    }
}

function fill_null_cards(){
    for (let y = 0; y < global_model.length ; y++) {
        for (let x = 0; x < global_model[y].length; x++) {
            if (global_model[y][x] === NULL_VALUE){
                global_model[y][x] = (Math.random() * (NUMBER_OF_CARDS - 1) + 1).toFixed(0);
            }
        }
    }
    update_grid();
}

function change_timer_value(difference) {
    global_timer += difference;
    if(is_game_over()) proceed_game_over();
    update_game_informations();
}

function proceed_game_over(){
    clearInterval(global_clock);
    alert("Game Over !");

    let leaderboard = [...global_leaderboard];
    // console.log(leaderboard);

    for (let i = 0; i < leaderboard.length; i++){
        if (parseInt(global_score) > parseInt(leaderboard[i][2])) {
            let player = prompt("You are position "+(i+1)+" in top 3 !\n Please enter your name to save your score :", "player");
            // console.log("lenght: "+leaderboard.length);
            for (let y = leaderboard.length - 1; y > i; y--) {
                let tmp = leaderboard[y][1];
                leaderboard[y][1] = leaderboard[y - 1][1];
                leaderboard[y - 1][1] = tmp;

                let tmp2 = leaderboard[y][2];
                leaderboard[y][2] = leaderboard[y - 1][2];
                leaderboard[y - 1][2] = tmp2;

                console.log("loop leaderboard iteration " + y);
                // console.log(leaderboard);
            }

            leaderboard[i][0] = global_leaderboard[i][0];
            leaderboard[i][1] = player;
            leaderboard[i][2] = global_score;
            // console.log(leaderboard);


            for (let y = 0; y < global_leaderboard.length; y++) {
                let request_post_score = new XMLHttpRequest();
                request_post_score.open('POST', 'requests/update_leaderboard.php', true);
                request_post_score.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                request_post_score.onreadystatechange = function () {
                    if (this.readyState === 4 && this.status === 200) {
                        // console.log(this.responseText);
                    }
                };
                request_post_score.send("id=" + global_leaderboard[y][0] + "&username=" + global_leaderboard[y][1] + "&score=" + global_leaderboard[y][2]);
            }
            break;
        }
    }

    start_game();
    get_data();
}

function proceed_good_permutation(number_of_good_cards){
    let timer = global_timer;
    timer += 10;
    if (number_of_good_cards >= NUMBER_OF_CARDS_TO_ALIGN + 2) {
        global_score += 1000 + 1000 * (global_level/10);
    }
    else if (number_of_good_cards === NUMBER_OF_CARDS_TO_ALIGN + 1) {
        global_score += 300 + 300 * (global_level/10);
    }
    else if (number_of_good_cards === NUMBER_OF_CARDS_TO_ALIGN) {
        global_score += 100 + 100 * (global_level/10);
    }

    while (timer >  100){
        global_level++;
        timer = timer - 100;
        update_game_informations();
    }

    global_timer = timer;
    update_game_informations();
}

function get_data(){
    let get_leaderboard_request = new XMLHttpRequest();
    get_leaderboard_request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            global_leaderboard = convert_json_to_array(this.responseText);
        }
    };
    get_leaderboard_request.open("GET", "requests/get_leaderboard.php", true);
    get_leaderboard_request.send();
}


// handle actions functions
function handle_action_card_permutation(event){

    if (global_is_paused){
        ELEMENT_BUTTON_PAUSE.innerHTML = '<i class="fas fa-pause"></i> Pause</i>';
        global_is_paused = false;
    }

    if (global_first_card === null){
        global_first_card = event.target.id;
        return;
    }
    global_second_card = event.target.id;

    let first_card_y = parseInt(global_first_card.match(/\d/g)[0]);
    let first_card_x = parseInt(global_first_card.match(/\d/g)[1]);

    let second_card_y = parseInt(global_second_card.match(/\d/g)[0]);
    let second_card_x = parseInt(global_second_card.match(/\d/g)[1]);
    global_first_card = null;
    global_second_card = null;

    // if the two selected cards
    if (second_card_x > first_card_x + 1 || second_card_x < first_card_x - 1 ||
        second_card_y > first_card_y + 1 || second_card_y < first_card_y - 1) {
        alert("You must select two cards next to each other.");
        return;
    }

    let first_card_value = global_model[first_card_y][first_card_x];
    let second_card_value = global_model[second_card_y][second_card_x];

    let saved_model = global_model;
    global_model[first_card_y][first_card_x] = second_card_value;
    global_model[second_card_y][second_card_x] = first_card_value;

    let good_sequences_card_coordinates = get_coordinates_of_cards_in_good_sequence();

    if (good_sequences_card_coordinates.length === 0){
        global_model = saved_model;
        global_tries_left--;
        update_game_informations();
    }
    else {
        tag_cards_in_good_sequences(good_sequences_card_coordinates);
        drop_cards();
        fill_null_cards();
        proceed_good_permutation(good_sequences_card_coordinates.length / 2);

        do {
            good_sequences_card_coordinates = get_coordinates_of_cards_in_good_sequence();
            tag_cards_in_good_sequences(good_sequences_card_coordinates);
            drop_cards();
            fill_null_cards();
            proceed_good_permutation(good_sequences_card_coordinates.length / 2);
        } while (good_sequences_card_coordinates.length !== 0);
    }
}

function handle_action_button_high_scores(){

    // get_data();

    let window_high_score = window.open('', '', "width=500, height=500, left=150, top=200, toolbar=1, status=1");

    let element_table_high_score = "";
    let element_row;

    element_table_high_score +=`<h1 style='border-collapse: collapse;
            text-align: center;
            height: 100px;'>High Scores</h1>
    `;
    element_table_high_score +="<div>";
    element_table_high_score += `<table 
        style='border-collapse: collapse;
            border-spacing: 0;
            margin-left:auto;
            margin-right:auto;
            width: 300px;
            position: relative;
            height: 100px;
            border: orange 1px solid;'>
    `;

    for (let i = 0; i < global_leaderboard.length; i++){
        element_row = "";
        element_row += "<tr>";
        element_row += "<td style='text-align: center; border: orange 1px solid;;'>"+global_leaderboard[i][0]+"</td>";
        element_row += "<td style='text-align: center; border: orange 1px solid;'>"+global_leaderboard[i][1]+"</td>";
        element_row += "<td style='text-align: center; border: orange 1px solid;'>"+global_leaderboard[i][2]+"</td>";
        element_row += "</tr>";
        element_table_high_score += element_row;
    }
    element_table_high_score += "</table>";
    element_table_high_score +="</div>";

    let node_body = window_high_score.document.getElementsByTagName("body")[0];
    node_body.innerHTML = element_table_high_score;

    node_body.innerHTML += `<button 
        style="
            text-align: center;
            position: center;
            display: inline-block;
            box-sizing: border-box;
            border: none;
            border-radius: 4px;
            padding: 0 16px;
            min-width: 64px;
            height: 36px;
            vertical-align: middle;
            text-overflow: ellipsis;
            text-transform: uppercase;
            color: #ffebee;
            background-color: #f44336;
            box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12);" 
        onclick='window.close()'>Close</button>`;

}

function handle_action_button_hint() {
    alert("hint");
}

function handle_action_button_pause_unpause_game(){
    if (global_is_paused) {
        global_is_paused = false;
        ELEMENT_BUTTON_PAUSE.innerHTML = '<i class="fas fa-pause"></i> Pause</i>';
        update_grid();
        add_event_listener_on_grid();
    }
    else {
        global_is_paused = true;
        ELEMENT_BUTTON_PAUSE.innerHTML = '<i class="fas fa-play"></i> Play';
        hide_grid();
        remove_event_listener_on_grid();
    }
}


// test game state functions
function is_game_over() {
    return global_timer <= 0 || global_tries_left <= 0;
}

// utility functions
function convert_json_to_array(json_format_string){
    let json = JSON.parse(json_format_string);

    let array_from_json = Array();
    for (let i = 0; i < json.length; i++) {
        array_from_json.push(Object.values(json[i]));
    }
    return array_from_json;
}