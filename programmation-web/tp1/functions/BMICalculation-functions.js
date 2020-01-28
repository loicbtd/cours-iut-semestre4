
function bind_crtl_c_BMICalculation(){
    let isCtrl = false;

    document.onkeyup = function(e){ 
        if(e.which == 17) {
            isCtrl=false; 
        }
    }
    
    document.onkeydown = function(e){
    
        if(e.which == 17) {
            isCtrl=true;
        }
    
        if(e.which == 67 && isCtrl == true) {
            calculate_BMICalculation()
        }
    }
}

// function enable_live_verification(){
//     document.getElementById("masse").addEventListener("onchange", function(){
//         validate_input();
//     });
//
//     document.getElementById("masse").addEventListener("onchange", function(){
//         validate_input();
//     });
// }


function validate_BMICalculation(){

    let hash = window.location.hash;


    let masse = document.getElementById("page-BMICalculation-input-mass").value;
    let taille = document.getElementById("page-BMICalculation-input-size").value;

    let isValid = true;

    if (masse == "") {
        if(hash.match(/-fr$/)) {
            alert("Le champ masse ne doit pas etre vide !");
        }
        else {
            alert("Field mass must not be empty !");
        }
        document.getElementById("page-BMICalculation-input-mass").style.border = "thick solid red";
        document.getElementById("page-BMICalculation-info-error-mass").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }

    if (taille == "") {
        if(hash.match(/-fr$/)) {
            alert("Le champ taille ne doit pas etre vide !");
        }
        else {
            alert("Field size must not be empty !");
        }
        document.getElementById("page-BMICalculation-input-size").style.border = "thick solid red";
        document.getElementById("page-BMICalculation-info-error-size").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }

    if (isNaN(masse)) {
        if(hash.match(/-fr$/)) {
            alert("Le champ masse doit contenir une valeur decimale !");
        }
        else {
            alert("Field mass must have a decimal value !");
        }
        document.getElementById("page-BMICalculation-input-mass").style.border = "thick solid red";
        document.getElementById("page-BMICalculation-info-error-mass").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }

    if (isNaN(taille)) {
        if(hash.match(/-fr$/)) {
            alert("Le champ taille doit contenir une valeur decimale !");
        }
        else {
            alert("Field size must have a decimal value !");
        }
        document.getElementById("page-BMICalculation-input-size").style.border = "thick solid red";
        document.getElementById("page-BMICalculation-info-error-size").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }

    if (masse <= 0) {
        if(hash.match(/-fr$/)) {
            alert("Le champ masse doit contenir une valeur positive !");
        }
        else {
            alert("Field mass must have a positive value !");
        }
        document.getElementById("page-BMICalculation-input-mass").style.border = "thick solid red";
        document.getElementById("page-BMICalculation-info-error-mass").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }

    if (taille <= 0) {
        if(hash.match(/-fr$/)) {
            alert("Le champ taille doit contenir une valeur positive !");
        }
        else {
            alert("Field size must have a positive value !");
        }
        document.getElementById("page-BMICalculation-input-size").style.border = "thick solid red";
        document.getElementById("page-BMICalculation-info-error-size").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }

    if (isValid) {
        document.getElementById("page-BMICalculation-info-error-mass").innerHTML = "<img src='./img/valid.png' width='15' height='15'>";
        document.getElementById("page-BMICalculation-info-error-size").innerHTML = "<img src='./img/valid.png' width='15' height='15'>";
    }

    return isValid;
}

function clear_BMICalculation(){
    document.getElementById("page-BMICalculation-input-mass").value = "";
    document.getElementById("page-BMICalculation-input-size").value = "";
}

function calculate_BMICalculation(){

    document.getElementById("page-BMICalculation-input-mass").style.border = "";
    document.getElementById("page-BMICalculation-input-size").style.border = "";

    document.getElementById("page-BMICalculation-info-error-mass").innerHTML = "";
    document.getElementById("page-BMICalculation-info-error-size").innerHTML = "";

    let masse = document.getElementById("page-BMICalculation-input-mass").value;
    let taille = document.getElementById("page-BMICalculation-input-size").value;
    let imc = masse/(taille*taille);

    let hash = window.location.hash;

    if(document.getElementById("page-BMICalculation-radio-female").checked){
        if (validate_BMICalculation(masse, taille)) {
            
            let etat;
    
            if (imc < 19.1) {
                if(hash.match(/-fr$/)) {
                    etat = "Maigreur";
                }
                else {
                    etat = "Underweight";
                }
            }
            else if (imc < 25.8) {
                if(hash.match(/-fr$/)) {
                    etat = "Poids idéal";
                }
                else {
                    etat = "Ideal weight";
                }
            }
            else if (imc < 27.3) {
                if(hash.match(/-fr$/)) {
                    etat = "À la limite du surpoids";
                }
                else {
                    etat = "Borderline overweight";
                }
            }
            else if (imc < 32.3) {
                if(hash.match(/-fr$/)) {
                    etat = "Surpoids";
                }
                else {
                    etat = "Overweight";
                }
            }
            else {
                if(hash.match(/-fr$/)) {
                    etat = "Surpoids";
                }
                else {
                    etat = "Obesity";
                }
                etat = "obesite severe";
            }

            if(hash.match(/-fr$/)) {
                document.getElementById("result").innerHTML = "Votre IMC est egale à " + imc.toFixed(2) + ". Remarque: " + etat;
            }
            else {
                document.getElementById("result").innerHTML = "Your BMI is equal to " + imc.toFixed(2) + ". Note: " + etat;

            }
        }
    }
    else {
        document.getElementById("page-BMICalculation-radio-male").checked = true;
        if (validate_BMICalculation(masse, taille)) {
            
            let etat;
    
            if (imc < 20.7) {
                if(hash.match(/-fr$/)) {
                    etat = "Maigreur";
                }
                else {
                    etat = "Underweight";
                }
            }
            else if (imc < 26.4) {
                if(hash.match(/-fr$/)) {
                    etat = "Poids idéal";
                }
                else {
                    etat = "Ideal weight";
                }
            }
            else if (imc < 27.8) {
                if(hash.match(/-fr$/)) {
                    etat = "À la limite du surpoids";
                }
                else {
                    etat = "Borderline overweight";
                }
            }
            else if (imc < 31.1) {
                if(hash.match(/-fr$/)) {
                    etat = "Surpoids";
                }
                else {
                    etat = "Overweight";
                }
            }
            else {
                if(hash.match(/-fr$/)) {
                    etat = "Surpoids";
                }
                else {
                    etat = "Obesity";
                }
                etat = "obesite severe";
            }

            if(hash.match(/-fr$/)) {
                document.getElementById("result").innerHTML = "Votre IMC est egale à " + imc.toFixed(2) + ". Remarque: " + etat;
            }
            else {
                document.getElementById("result").innerHTML = "Your BMI is equal to " + imc.toFixed(2) + ". Note: " + etat;

            }
        }
    }    
}


