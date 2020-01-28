var DevoirVue = (function() {
    pageDevoir = document.getElementById("page-devoir").innerHTML;

    return function(devoir) {
        this.afficher = function() {
            elementBody = document.getElementsByTagName("body")[0];
            elementBody.innerHTML = pageDevoir;
            
            document.getElementById("devoir-nom").innerHTML = devoir.nom;
            document.getElementById("devoir-matiere").innerHTML = devoir.matiere;
            document.getElementById("devoir-description").innerHTML = devoir.description;
        }
    }
})();