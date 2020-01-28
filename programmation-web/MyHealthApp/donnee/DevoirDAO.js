var DevoirDAO = function() {

    var listeDevoir = null;

    var initialiser = function() {
        if(!listeDevoir) {
            listeDevoir = [];
        }
    }

    this.lister = function() {
        if(localStorage['devoir']) {
            listeDevoir = JSON.parse(localStorage['devoir']);
        }

        for(position in listeDevoir) {
            var devoir = new Devoir(
                listeDevoir[position].nom,
                listeDevoir[position].matiere,
                listeDevoir[position].description,
                listeDevoir[position].id
            );

            listeDevoir[position] = devoir;
        }

        return listeDevoir;
    }

    this.ajouter = function(devoir) {
        if(listeDevoir.length > 0) {
            devoir.id = listeDevoir[listeDevoir.length-1].id + 1;
        }
        else {
            devoir.id = 0;
        }
        
        listeDevoir[devoir.id] = devoir;
        localStorage['devoir'] = JSON.stringify(listeDevoir);
    }


    this.modifier = function(devoir) {        
        listeDevoir[devoir.id] = devoir;
        localStorage['devoir'] = JSON.stringify(listeDevoir);
    }

    initialiser();
}