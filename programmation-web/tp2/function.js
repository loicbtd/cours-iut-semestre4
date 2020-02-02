function transformer_chaine_en_vecteur(chaine,separateur){
    return chaine.split(separateur);
}

function recuperer_donnees_client(code) {
    let xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            document.getElementById("txtHint").innerHTML = this.responseText;
        }
    };
    xmlHttpRequest.open("GET", "getclient.php?code="+code, true);
    xmlHttpRequest.send();
}

(function (){
    transformer_chaine_en_vecteur("oui;oui",";");
    recuperer_donnees_client(1);
}());