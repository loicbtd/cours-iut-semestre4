function clear_FactorialCalculation(){
    document.getElementById("page-FactorialCalculation-input-value").value = "";
    document.getElementById("page-FactorialCalculation-result").innerHTML = "";
}


function factorial(n){
    let j = 1;
    for(let i=1; i<=n; i++){
        j = j*i;
    }
    return j;
}

function calculate_FactorialCalculation(){
    let input_value = document.getElementById("page-FactorialCalculation-input-value").value;
    document.getElementById("page-FactorialCalculation-result").innerHTML = factorial(input_value);
}