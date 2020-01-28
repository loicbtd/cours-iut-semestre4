function naviguer() {
    let hash = window.location.hash;

    let elementBody = document.getElementsByTagName("body")[0];

    elementBody.innerHTML = fragmentNavbar;

    if(hash.match(/-fr$/)) {
        // setup actions descriptions
        document.getElementById("action-button-navbar").innerHTML = "Calculer";
        document.getElementById("clear-button-navbar").innerHTML = "Effacer les champs";
        document.getElementById("print-button-navbar").innerHTML = "Imprimer";

        // setup navigation descriptions
        document.getElementById("nav-action").innerHTML = "Actions";
        document.getElementById("nav-modes").innerHTML = "Modes";
        document.getElementById("nav-help").innerHTML = "Aide";
        document.getElementById("action-navigate-BMICalculation").innerHTML = "Calcul IMC";
        document.getElementById("action-navigate-FactorialCalculation").innerHTML = "Calcul Factoriel";
        document.getElementById("action-navigate-FibonacciCalculation").innerHTML = "Calcul Fibonacci";
        document.getElementById("action-navigate-Converter").innerHTML = "Convertisseur";
        document.getElementById("action-navigate-SiteDescription").innerHTML = "Description du site";
        document.getElementById("action-navigate-ContactUs").innerHTML = "Contactez-nous";
        document.getElementById("action-navigate-language").innerHTML = "<img src='img/flag-uk.png' width='40' height='30' alt=''>"      
        
        // setup navigation links
        document.getElementById("action-navigate-BMICalculation").href = "#BMICalculation-fr";
        document.getElementById("action-navigate-FactorialCalculation").href = "#FactorialCalculation-fr";
        document.getElementById("action-navigate-FibonacciCalculation").href = "#FibonacciCalculation-fr";
        document.getElementById("action-navigate-SiteDescription").href = "#SiteDescription-fr";
        document.getElementById("action-navigate-ContactUs").href = "#ContactUs-fr";
        document.getElementById("action-navigate-language").href = hash.replace(/-fr/i, "-en");        
    }
    else {
        // setup actions descriptions
        document.getElementById("action-button-navbar").innerHTML = "Calculate";
        document.getElementById("clear-button-navbar").innerHTML = "Clear fields";
        document.getElementById("print-button-navbar").innerHTML = "Print";
        
        // setup navigation descriptions
        document.getElementById("nav-action").innerHTML = "Actions";
        document.getElementById("nav-modes").innerHTML = "Modes";
        document.getElementById("nav-help").innerHTML = "Help";
        document.getElementById("action-navigate-BMICalculation").innerHTML = "Calculate BMI";
        document.getElementById("action-navigate-FactorialCalculation").innerHTML = "Calculate Factorial";
        document.getElementById("action-navigate-FibonacciCalculation").innerHTML = "Calculate Fibonacci";
        document.getElementById("action-navigate-Converter").innerHTML = "Converter";
        document.getElementById("action-navigate-SiteDescription").innerHTML = "Site description";
        document.getElementById("action-navigate-ContactUs").innerHTML = "Contact us";
        document.getElementById("action-navigate-language").innerHTML = "<img src='img/flag-fr.png' width='40' height='30' alt=''>"      
        
        // setup navigation links
        document.getElementById("action-navigate-BMICalculation").href = "#BMICalculation-en";
        document.getElementById("action-navigate-FactorialCalculation").href = "#FactorialCalculation-en";
        document.getElementById("action-navigate-FibonacciCalculation").href = "#FibonacciCalculation-en";
        document.getElementById("action-navigate-SiteDescription").href = "#SiteDescription-en";
        document.getElementById("action-navigate-ContactUs").href = "#ContactUs-en";
        document.getElementById("action-navigate-language").href = hash.replace(/-en/i, "-fr");
    }

    if(hash.match(/^#BMICalculation-fr/)){
        elementBody.innerHTML += pageBMICalculation;

        // setup navbar events
        document.getElementById("action-button-navbar").addEventListener("click", calculate_BMICalculation);
        document.getElementById("clear-button-navbar").addEventListener("click", clear_BMICalculation);

        // fill innerHTML
        document.getElementById("page-BMICalculation-title").innerHTML = "Calcul de l'indice de masse corporelle";
        document.getElementById("page-BMICalculation-instructions").innerHTML = "Insérez votre masse en KG et votre taille en m dans les deux champs de texte suivants:";
        document.getElementById("page-BMICalculation-label-mass").innerHTML = "Masse (Kg)";
        document.getElementById("page-BMICalculation-label-size").innerHTML = "Taille (cm)";
        document.getElementById("page-BMICalculation-label-gender").innerHTML = "Sexe";
        document.getElementById("page-BMICalculation-label-male").innerHTML = "Homme";
        document.getElementById("page-BMICalculation-label-female").innerHTML = "Femme";
        document.getElementById("page-BMICalculation-button-calculate").innerHTML = "Calculer";
        document.getElementById("page-BMICalculation-button-clear").innerHTML = "Effacer";

        // add event listener
        document.getElementById("page-BMICalculation-button-calculate").addEventListener("mouseover", function(){
            document.getElementById("page-BMICalculation-button-calculate").title = "appuyer sur le boutton pour calculer";
        });
        document.getElementById("page-BMICalculation-button-clear").addEventListener("click", clear_BMICalculation);
        document.getElementById("page-BMICalculation-button-calculate").addEventListener("click", calculate_BMICalculation);
        bind_crtl_c_BMICalculation();
    }
    else if(hash.match(/^#BMICalculation-en/)){
        elementBody.innerHTML += pageBMICalculation;

         // setup navbar events
         document.getElementById("action-button-navbar").addEventListener("click", calculate_BMICalculation);
         document.getElementById("clear-button-navbar").addEventListener("click", clear_BMICalculation);
         // document.getElementById("print-button-navbar").addEventListener("click", print_BMICalculation);

        // fill innerHTML
        document.getElementById("page-BMICalculation-title").innerHTML = "BMI calculation";
        document.getElementById("page-BMICalculation-instructions").innerHTML = "Input your mass in Kg and your size in meters into the two following fields:";
        document.getElementById("page-BMICalculation-label-mass").innerHTML = "Masse (Kg)";
        document.getElementById("page-BMICalculation-label-size").innerHTML = "Size (cm)";
        document.getElementById("page-BMICalculation-label-gender").innerHTML = "Gender";
        document.getElementById("page-BMICalculation-label-male").innerHTML = "Male";
        document.getElementById("page-BMICalculation-label-female").innerHTML = "Female";
        document.getElementById("page-BMICalculation-button-calculate").innerHTML = "Calculate";
        document.getElementById("page-BMICalculation-button-clear").innerHTML = "Clear";

        // add event listener
        document.getElementById("page-BMICalculation-button-calculate").addEventListener("mouseover", function(){
            document.getElementById("page-BMICalculation-button-calculate").title = "press the button to calculate";
        });
        document.getElementById("page-BMICalculation-button-clear").addEventListener("click", clear_BMICalculation);
        document.getElementById("page-BMICalculation-button-calculate").addEventListener("click", calculate_BMICalculation);
        bind_crtl_c_BMICalculation();
    }

    else if(hash.match(/^#Converter-fr/)){
        elementBody.innerHTML += pageConverter;
    }
    else if(hash.match(/^#Converter-en/)){
        elementBody.innerHTML += pageConverter;
    }
    else if(hash.match(/^#FactorialCalculation-fr/)){
        elementBody.innerHTML += pageFactorialCalculation;
    }
    else if(hash.match(/^#FactorialCalculation-en/)){
        elementBody.innerHTML += pageFactorialCalculation;
    }
    else if(hash.match(/^#FibonacciCalculation-fr/)){
        elementBody.innerHTML += pageFibonacciCalculation;
    }
    else if(hash.match(/^#FibonacciCalculation-en/)){
        elementBody.innerHTML += pageFibonacciCalculation;
    }
    else if(hash.match(/^#SiteDescription-fr/)){
        elementBody.innerHTML += pageSiteDescription;
        
        document.getElementById("page-SiteDescription-title").innerHTML = "Description du Site";
    }
    else if(hash.match(/^#SiteDescription-en/)){
        elementBody.innerHTML += pageSiteDescription;
        document.getElementById("page-SiteDescription-title").innerHTML = "Site description";
    }
    else if(hash.match(/^#ContactUs-fr/)){
        elementBody.innerHTML += pageContactUs;
    }
    else if(hash.match(/^#ContactUs-en/)){
        elementBody.innerHTML += pageContactUs;
    }
    else {
        window.location.hash = "BMICalculation-fr";
    }
}

(function() {
    elementBody = document.getElementsByTagName("body")[0];
    
    fragmentNavbar = document.getElementById("fragment-navbar").innerHTML;

    pageBMICalculation = document.getElementById("page-BMICalculation").innerHTML;
    pageContactUs = document.getElementById("page-ContactUs").innerHTML;
    pageConverter = document.getElementById("page-Converter").innerHTML;
    pageFactorialCalculation = document.getElementById("page-FactorialCalculation").innerHTML;
    pageFibonacciCalculation = document.getElementById("page-FibonacciCalculation").innerHTML;
    pageSiteDescription = document.getElementById("page-SiteDescription").innerHTML;
    window.addEventListener("hashchange", naviguer);
    naviguer();
})();