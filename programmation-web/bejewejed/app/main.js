function generate_grid(){
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

function reset_grid() {
    for (let y = 0; y < grid_size_y; y++) {
        for (let x = 0; x < grid_size_x; x++) {
            let cell = document.getElementById("cell-row-"+y+"-col-"+x);
                cell.innerHTML += "<img src='resources/images/red.png' width='60' height='50'>";
        }
    }
}

(function () {
    element_container_header = document.getElementById("container-header");
    element_container_grid = document.getElementById("container-grid");
    element_container_progressbar = document.getElementById("container-progressbar");
    grid_size_x = 8;
    grid_size_y = 8;
    generate_grid(grid_size_x, grid_size_y);
    reset_grid();
})();