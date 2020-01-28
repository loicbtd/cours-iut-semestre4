(function() {

    var devoirDAO = null;

    var initialiser = function initialiser() {
        window.addEventListener("hashchange", naviguer);
        devoirDAO = new DevoirDAO();
        naviguer();
    };

    var naviguer = function() {
        var hash = window.location.hash;

        if(!hash) {
            var listeDevoirDonnee = devoirDAO.lister();
            var listeDevoirVue = new ListeDevoirVue(listeDevoirDonnee);
            listeDevoirVue.afficher();
        }
        else if(hash.match(/^#ajouter-devoir/)) {
            var ajouterDevoirVue = new AjouterDevoirVue(actionAjouterDevoir);
            ajouterDevoirVue.afficher();
        }
        else if(hash.match(/^#modifier-devoir\/([0-9]+)/)){
            var navigation = hash.match(/^#modifier-devoir\/([0-9]+)/);
            var idDevoir = navigation[1];
            
            var listeDevoirDonnee = devoirDAO.lister();
            var modifierDevoirVue = new ModifierDevoirVue(listeDevoirDonnee[idDevoir], actionModifierDevoir);
            modifierDevoirVue.afficher();
        }
        else {
            var navigation = hash.match(/^#devoir\/([0-9]+)/);
            var idDevoir = navigation[1];
            
            var listeDevoirDonnee = devoirDAO.lister();
            var devoirVue = new DevoirVue(listeDevoirDonnee[idDevoir]);
            devoirVue.afficher();
        }
    }

    var actionAjouterDevoir = function(devoir) {
        devoirDAO.ajouter(devoir);
        window.location.hash = "#";
    }

    var actionModifierDevoir = function(devoir) {
        devoirDAO.modifier(devoir);
        window.location.hash = "#";
    }

    initialiser();
})();