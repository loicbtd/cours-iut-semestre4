function clear_FibonacciCalculation(){
    document.getElementById("page-FibonacciCalculation-input-value").value = "";
    document.getElementById("page-FibonacciCalculation-result").innerHTML = "";
}

function fibonacci(num){
    let suite = [];
    var a = 1, b = 0, temp;

    while (num >= 0){
        temp = a;
        a = a + b;
        b = temp;
        num--;
        suite.push(b + " ");
    }

    return suite;
}

function calculate_FibonacciCalculation(){
    let input_value = document.getElementById("page-FibonacciCalculation-input-value").value;
    document.getElementById("page-FibonacciCalculation-result").innerHTML = fibonacci(input_value);
}