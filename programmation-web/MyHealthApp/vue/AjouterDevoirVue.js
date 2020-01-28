var AjouterDevoirVue = (function() {
    pageAjouterDevoir = document.getElementById("page-ajouter-devoir").innerHTML;

    return function(actionAjouterDevoir) {
        this.afficher = function() {
            elementBody = document.getElementsByTagName("body")[0];
            elementBody.innerHTML = pageAjouterDevoir;
            
            var formulaireAjouter = document.getElementById("formulaire-ajouter");
            formulaireAjouter.addEventListener("submit", ajouter);
        
        }
        
        var ajouter = function(evenement) {
            evenement.preventDefault();

            var nom = document.getElementById("devoir-nom").value;
            var matiere = document.getElementById("devoir-matiere").value;
            var description = document.getElementById("devoir-description").value;
            
            var devoir = new Devoir(nom, matiere, description, null);

            actionAjouterDevoir(devoir);
        }
    }
})();