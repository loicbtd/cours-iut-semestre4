function validate_input(masse, taille){
    let isValid = true;

    if (masse == "") {
        alert("Le champ masse ne doit pas etre vide !");
        document.getElementById("masse").style.border = "thick solid red";
        document.getElementById("info-erreur-masse").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }
    
    if (taille == "") {
        alert("Le champ taille ne doit pas etre vide !");
        document.getElementById("taille").style.border = "thick solid red";
        document.getElementById("info-erreur-taille").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }
    
    if (isNaN(masse)) {
        alert("Le champ masse doit contenir une valeur decimale !");
        document.getElementById("masse").style.border = "thick solid red";
        document.getElementById("info-erreur-masse").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }
    
    if (isNaN(taille)) {
        alert("Le champ taille doit contenir une valeur decimale !");
        document.getElementById("taille").style.border = "thick solid red";
        document.getElementById("info-erreur-taille").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }
    
    if (masse <= 0) {
        alert("La masse doit etre positive !");
        document.getElementById("masse").style.border = "thick solid red";
        document.getElementById("info-erreur-masse").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }
    
    if (taille <= 0) {
        alert("La taille doit etre positive !");        
        document.getElementById("taille").style.border = "thick solid red";
        document.getElementById("info-erreur-taille").innerHTML = "<img src='./img/error.png' width='15' height='15'>";
        isValid = false;
    }
    
    if (isValid) {
        document.getElementById("info-erreur-masse").innerHTML = "<img src='./img/valid.png' width='15' height='15'>";
        document.getElementById("info-erreur-taille").innerHTML = "<img src='./img/valid.png' width='15' height='15'>";

    }

    return isValid;
}

function clear_data(){
    document.getElementById("masse").value = "";
    document.getElementById("taille").value = "";
}

function calculate_imc(){

    document.getElementById("masse").style.border = "";
    document.getElementById("taille").style.border = "";
    
    document.getElementById("info-erreur-masse").innerHTML = "";
    document.getElementById("info-erreur-taille").innerHTML = "";

    let masse = document.getElementById("masse").value;
    let taille = document.getElementById("taille").value;

    if (validate_input(masse, taille)) {
        let imc = masse/(taille*taille);
        let etat;

        if (imc < 18.5) {
            etat = "maigre";
        }
        else if (imc < 25) {
            etat = "normal chez un adulte";
        }
        else if (imc < 30) {
            etat = "surpoids (surcharge ponderale)";
        }
        else if (imc < 35) {
            etat = "obesite";
        }
        else if (imc < 40) {
            etat = "obesite severe";
        }
        else {
            etat = "obesite morbide";
        }
        document.getElementById("resultat").innerHTML = "Votre IMC est egale a " + imc.toFixed(2) + ". Remarque: " + etat;
    }
}


function bind_crtl_c(){
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
            calculate_imc()
        }
    }
}

function enable_button_advise(){
    document.getElementById("bouton-calculer").addEventListener("mouseover", function(){
        document.getElementById("bouton-calculer").title = "appuyer sur le boutton pour calculer";
    });
}

function enable_live_verification(){
    document.getElementById("masse").addEventListener("onchange", function(){
        vali
    });

    document.getElementById("masse").addEventListener("onchange", function(){

    });
}


(function() {
    bind_crtl_c();
    enable_button_advise();
})();