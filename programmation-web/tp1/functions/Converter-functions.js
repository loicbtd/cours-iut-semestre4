function calculate_Converter(){
    let input_value = document.getElementById("page-Converter-input-value").value;
    let conversion_type = document.getElementById("page-Converter-dropdown-type").value;
    let result;
    switch (conversion_type) {
        case '1':
            result = input_value / 2.54;
            break;
        case '2':
            result = input_value * 2.205;
            break;
        case '3':
            result = input_value / 1.609;
            break;
        case '4':
            result = input_value * (5/9) + 32;
            break;
        case '5':
            result = input_value * 2.54;
            break;
        case '6':
            result = input_value / 2.205;
            break;
        case '7':
            result = input_value * 1.609;
            break;
        case '8':
            result = (input_value - 32) * (5/9);
            break;
    }
    console.log(result);
    document.getElementById("page-Converter-result").innerHTML = Math.round(result);
}
function clear_Converter(){
    document.getElementById("page-Converter-input-value").value = "";
    document.getElementById("page-Converter-result").innerHTML = "";
}

function invert_Converter(){
    let conversion_type = document.getElementById("page-Converter-dropdown-type").value;
    switch (conversion_type) {
        case '1':
            document.getElementById("page-Converter-type1").selected = "";
            document.getElementById("page-Converter-type5").selected = "selected";
            break;
        case '2':
            document.getElementById("page-Converter-type2").selected = "";
            document.getElementById("page-Converter-type6").selected = "selected";
            break;
        case '3':
            document.getElementById("page-Converter-type3").selected = "";
            document.getElementById("page-Converter-type7").selected = "selected";
            break;
        case '4':
            document.getElementById("page-Converter-type4").selected = "";
            document.getElementById("page-Converter-type8").selected = "selected";
            break;
        case '5':
            document.getElementById("page-Converter-type5").selected = "";
            document.getElementById("page-Converter-type1").selected = "selected";
            break;
        case '6':
            document.getElementById("page-Converter-type6").selected = "";
            document.getElementById("page-Converter-type2").selected = "selected";
            break;
        case '7':
            document.getElementById("page-Converter-type7").selected = "";
            document.getElementById("page-Converter-type3").selected = "selected";
            break;
        case '8':
            document.getElementById("page-Converter-type8").selected = "";
            document.getElementById("page-Converter-type4").selected = "selected";
            break;
    }
}
