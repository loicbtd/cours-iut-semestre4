var ModifierDevoirVue = (function() {
    pageModifierDevoir = document.getElementById("page-modifier-devoir").innerHTML;

    return function(devoir, actionModifierDevoir) {
        this.afficher = function() {
            elementBody = document.getElementsByTagName("body")[0];
            elementBody.innerHTML = pageModifierDevoir;

            document.getElementById("devoir-nom").value = devoir.nom;
            document.getElementById("devoir-matiere").value = devoir.matiere;
            document.getElementById("devoir-description").value = devoir.description;
            
            var formulaireModifier = document.getElementById("formulaire-modifier");
            formulaireModifier.addEventListener("submit", modifier);
        
        }
        
        var modifier = function(evenement) {
            evenement.preventDefault();

            var nom = document.getElementById("devoir-nom").value;
            var matiere = document.getElementById("devoir-matiere").value;
            var description = document.getElementById("devoir-description").value;
            var id = window.location.hash.match(/^#modifier-devoir\/([0-9]+)/)[1];

            var devoir = new Devoir(nom, matiere, description, id);

            actionModifierDevoir(devoir);
        }
    }
})();