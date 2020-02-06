function transformer_chaine_en_vecteur(chaine,separateur){
    let lignes = chaine.split("\n");
    let vecteur = Array();
    for(let i=0; i<lignes.length; i++) {
        vecteur.push(lignes[i].split(separateur));
    }
    return vecteur;
}

function trouver_enregistrement_par_id(enregistrements, id){
    for (let i = 0; i < enregistrements.length; i++) {
        if (enregistrements[i][0] === id) {
            return enregistrements[i];
        }
    }
    return null;
}

function mettre_a_jour_ligne(numero_ligne){

    let code_service = document.getElementById("choix-prestation-ligne-" + numero_ligne).value;

    if(code_service === '0'){
        document.getElementById("code-prestation-ligne-"+numero_ligne).innerHTML = "";
        document.getElementById("prix-ligne-"+numero_ligne).innerHTML = "-";
        document.getElementById("montant-ligne-"+numero_ligne).innerHTML = "-";
        return
    }

    let service = trouver_enregistrement_par_id(services, code_service);

    let quantite = document.getElementById("quantite-ligne-"+numero_ligne).value;

    let prix = parseFloat(service[2]);

    let montant = prix * quantite;
    montant = montant.toFixed(2);

    if (isNaN(montant)) {
        montant = 0;
    }

    document.getElementById("code-prestation-ligne-"+numero_ligne).innerHTML = service[0];
    document.getElementById("prix-ligne-"+numero_ligne).innerHTML = service[2];
    document.getElementById("montant-ligne-"+numero_ligne).innerHTML = montant;

    mettre_a_jour_total();
}

function mettre_a_jour_total(){
    let nombre_ligne = document.getElementsByClassName("ligne-tableau").length;

    let somme = 0;

    let montant_ligne
    for (let i = 1; i < nombre_ligne + 1; i++) {
        montant_ligne = document.getElementById("montant-ligne-"+i).innerHTML;
        if(!isNaN(montant_ligne)){
            somme += parseFloat(montant_ligne);
        }
    }
    document.getElementById("somme").innerHTML = somme.toFixed(2);
    mettre_a_jour_a_regler();
}

function mettre_a_jour_reduction(code_client){
    let remise = trouver_enregistrement_par_id(clients, code_client)[8];
    document.getElementById("remise").innerHTML = remise;
    mettre_a_jour_a_regler();
}

function mettre_a_jour_a_regler() {
    let a_regler;
    let somme = parseFloat(document.getElementById("somme").innerHTML);
    let remise = document.getElementById("remise").innerHTML;

    if (!isNaN(remise) && !isNaN(somme)) {
        remise = parseFloat(remise);
        a_regler = somme - (somme * remise) / 100;
        document.getElementById("a-regler").innerHTML = a_regler.toFixed(2);
    } else if (!isNaN(somme)) {
        a_regler = somme;
        document.getElementById("a-regler").innerHTML = a_regler.toFixed(2);
    } else {
        document.getElementById("a-regler").innerHTML = "-";
    }
}

function ajouter_ligne(){

    let quantites = Array();
    let value;

    let prestations = Array();
    let prestation;

    for (let i = 0; i < document.getElementsByClassName("ligne-tableau").length; i++) {
        value = document.getElementById("quantite-ligne-"+(i+1)).value;
        if (isNaN(value)) {
            value = "";
        }
        else {
            quantites.push(value);
        }
        prestation = document.getElementById("choix-prestation-ligne-"+(i+1)).value;
        prestations.push(prestation);
    }

    let services_elements_option;

    services_elements_option += "<option value='0'>vide  </option>";
    for (let i = 0; i < services.length; i++) {
        services_elements_option += "<option value='" + services[i][0] + "'>" + services[i][1] + "</option>";
    }

    let numero_ligne =  document.getElementsByClassName("ligne-tableau").length + 1;

    document.getElementById("tableau").innerHTML += `            
        <tr id='ligne-`+numero_ligne+`' class="ligne-tableau">
            <td style='border: 1px solid black;' id="code-prestation-ligne-`+numero_ligne +`"></td>
            <td style='border: 1px solid black;'>
                <select id='choix-prestation-ligne-`+numero_ligne +`' style='width: 80%;' onchange='mettre_a_jour_ligne(`+numero_ligne+`)'>
                  `+services_elements_option+`
                </select>
            </td>
            <td style='border: 1px solid black;'><div style="display: inline;" id='prix-ligne-`+numero_ligne+`'>-</div> €</td>
            <td style='border: 1px solid black;'>
                <input style="text-align: center;" id='quantite-ligne-`+numero_ligne +`' type='text' oninput='mettre_a_jour_ligne(`+numero_ligne+`)'>
            </td>
            <td style='border: 1px solid black;'><div style="display: inline;" id='montant-ligne-`+numero_ligne +`'>-</div> €</td>
        </tr>`;

    for (let i = 0; i < quantites.length; i++) {
        if (!isNaN(quantites[i])) {
            document.getElementById("quantite-ligne-"+(i+1)).value = quantites[i];
            document.getElementById("choix-prestation-ligne-"+(i+1)).value = prestations[i];
        }
    }
}

function supprimer_ligne(){

    let numero_ligne =  document.getElementsByClassName("ligne-tableau").length;
    if (numero_ligne === 0) return;

    let ligne = document.getElementById("ligne-"+numero_ligne);
    ligne.parentNode.removeChild(ligne);
}

function recuperer_donnees_client() {

    let code = document.getElementById("code-client").value;
    let client = trouver_enregistrement_par_id(clients, code);

    if (client != null) {
        document.getElementById("civilite").innerHTML = client[1] + " ";
        document.getElementById("nom").innerHTML = client[2] + " ";
        document.getElementById("prenom").innerHTML = client[3];
        document.getElementById("adresse").innerHTML = client[4];
        document.getElementById("code-postal").innerHTML = client[5] + " ";
        document.getElementById("ville").innerHTML = client[6];
        document.getElementById("carte").innerHTML = "Votre carte est " + client[7] + ".";
        mettre_a_jour_reduction(code);
    }
    else {
        document.getElementById("civilite").innerHTML = "";
        document.getElementById("nom").innerHTML = "";
        document.getElementById("prenom").innerHTML = "";
        document.getElementById("adresse").innerHTML = "";
        document.getElementById("code-postal").innerHTML = "";
        document.getElementById("ville").innerHTML = "";
        document.getElementById("carte").innerHTML = "";
        document.getElementById("remise").innerHTML = "-";
    }
    recuperer_commandes_client();
}

function creer_nouvelle_facture(){
    let nombre_lignes = document.getElementsByClassName("ligne-tableau").length;

    for (let i = 0; i < nombre_lignes; i++) {
        supprimer_ligne();
    }
    ajouter_ligne();
    mettre_a_jour_a_regler();
}

function sauvegarder(){

    let code_client = document.getElementById("code-client").value;
    if (trouver_enregistrement_par_id(clients, code_client) == null) {
        alert("Impossible de sauvegarder, vérifiez vos saisies");
        return;
    }

    let nombre_lignes = document.getElementsByClassName("ligne-tableau").length;
    let contient = Array();
    let code_produit;
    let quantite;
    for (let i = 1; i < nombre_lignes + 1; i++) {
        code_produit = document.getElementById("code-prestation-ligne-"+i).innerHTML;
        quantite = document.getElementById("quantite-ligne-"+i).value;
        if(code_produit === "") continue;
        if(quantite === "") continue;
        if(isNaN(code_produit)) continue;
        if(isNaN(quantite)) continue;
        contient.push([code_produit, quantite]);
    }

    if (contient.length === 0) {
        alert("Impossible de sauvegarder, vérifiez vos saisies");
        return;
    }

    let prix_total = document.getElementById("a-regler").innerHTML;
    let date_commande = document.getElementById("date").innerHTML;
    let body = prix_total + ";" + date_commande + ";" + code_client + "|";
    for (let i = 0; i < contient.length; i++) {
        body += contient[i][0] + "," + contient[i][1] + ";"
    }
    body = body.substring(0, body.length - 1);
    // console.log(body);

    // prix_total;date_commande;code_client|code_produit,quantite;code_produit,quantite

    let requete_post_commande = new XMLHttpRequest();
    requete_post_commande.open('POST', 'postcommande.php', true);
    requete_post_commande.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    requete_post_commande.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            console.log(this.responseText);
        }
    };
    let num_commande = document.getElementById("liste-deroulante-commande").value;
    if (num_commande === "-1"){
        requete_post_commande.send("var="+body);
    }
    else {
        requete_post_commande.send("var="+body+"&num_commande="+num_commande);
    }
    alert("Sauvegardé avec succès !");
}

function recuperer_commandes_client(){
    let code_client = document.getElementById("code-client").value;
    if (trouver_enregistrement_par_id(clients, code_client) == null) {
        document.getElementById("zone-commandes").innerHTML = "";
        return;
    }

    let commandes_du_client = Array();
    for (let i = 0; i < commandes.length; i++) {
        if(commandes[i][3] === code_client){
            commandes_du_client.push(commandes[i])
        }
    }

    let elements_option = "";
    for (let i = 0; i < commandes_du_client.length; i++) {
        elements_option += "<option value='" + commandes_du_client[i][0] + "'>" + "commande n°" + commandes_du_client[i][0] + " du " + commandes_du_client[i][2] + "</option>";
    }

    document.getElementById("zone-commandes").innerHTML = `
        <span>Commande du client courant: </span>
        <select onchange="charger_commande()" id="liste-deroulante-commande">
            <option id="option-commande-courante" value="-1">commande courante</option>
            `+elements_option+`
        </select>`;
}

function charger_commande() {
    let element_commande_courante = document.getElementById("option-commande-courante");
    if (element_commande_courante != null){
        element_commande_courante.parentNode.removeChild(element_commande_courante);
    }

    creer_nouvelle_facture();

    // on recupere le numero de la commande
    let num_commande = document.getElementById("liste-deroulante-commande").value;

    // on recupere le contenu de la commande
    let contient_commande_courante = Array();
    for (let i = 0; i < contient.length; i++) {
        if (num_commande === contient[i][0]) {
            contient_commande_courante.push(contient[i])
        }
    }

    // on recuperer la liste des services
    let services_elements_option;
    services_elements_option += "<option value='0'>vide  </option>";
    for (let i = 0; i < services.length; i++) {
        services_elements_option += "<option value='" + services[i][0] + "'>" + services[i][1] + "</option>";
    }

    // remplissage du tableau
    for (let i = 0; i < contient_commande_courante.length; i++) {
        // on recupere le numero de la nouvelle ligne
        let numero_ligne =  document.getElementsByClassName("ligne-tableau").length + 1;

        // on remplie le tableau
        document.getElementById("tableau").innerHTML += `
        <tr id='ligne-`+numero_ligne+`' class="ligne-tableau">
            <td style='border: 1px solid black;' id="code-prestation-ligne-`+numero_ligne +`"></td>
            <td style='border: 1px solid black;'>
                <select id='choix-prestation-ligne-`+numero_ligne +`' style='width: 80%;' onchange='mettre_a_jour_ligne(`+numero_ligne+`)'>
                  `+services_elements_option+`
                </select>
            </td>
            <td style='border: 1px solid black;'><div style="display: inline;" id='prix-ligne-`+numero_ligne+`'>-</div> €</td>
            <td style='border: 1px solid black;'>
                <input style="text-align: center;" id='quantite-ligne-`+numero_ligne +`' type='text' oninput='mettre_a_jour_ligne(`+numero_ligne+`)'>
            </td>
            <td style='border: 1px solid black;'><div style="display: inline;" id='montant-ligne-`+numero_ligne +`'>-</div> €</td>
        </tr>`;
    }


    for (let i = 0; i < contient_commande_courante.length; i++) {
        document.getElementById("quantite-ligne-"+(i+1)).value = contient_commande_courante[i][2];
        document.getElementById("choix-prestation-ligne-"+(i+1)).value = contient_commande_courante[i][1];
        mettre_a_jour_ligne(i+1)
    }

    supprimer_ligne();
}

(function (){
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0');  //January is 0!
    let yyyy = today.getFullYear();
    today = mm + '/' + dd + '/' + yyyy;
    document.getElementById("date").innerHTML = today;

    clients = Array();
    services = Array();
    commandes = Array();
    contient = Array();

    let requete_client = new XMLHttpRequest();
    requete_client.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            clients = transformer_chaine_en_vecteur(this.responseText, ',');
        }
    };
    requete_client.open("GET", "getclient.php", true);
    requete_client.send();

    let requete_service = new XMLHttpRequest();
    requete_service.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            services = transformer_chaine_en_vecteur(this.responseText, ',');
        }
    };
    requete_service.open("GET", "getservice.php", true);
    requete_service.send();

    let requete_commandes = new XMLHttpRequest();
    requete_commandes.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            commandes = transformer_chaine_en_vecteur(this.responseText, ',');
            ajouter_ligne();
        }
    };
    requete_commandes.open("GET", "getcommande.php", true);
    requete_commandes.send();

    let requete_contient = new XMLHttpRequest();
    requete_contient.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            contient = transformer_chaine_en_vecteur(this.responseText, ',');
        }
    };
    requete_contient.open("GET", "getcontient.php", true);
    requete_contient.send();

    document.getElementById("code-client").addEventListener("input", recuperer_donnees_client);
    document.getElementById("bouton-ajouter-ligne").addEventListener("click", ajouter_ligne);
    document.getElementById("bouton-supprimer-ligne").addEventListener("click", supprimer_ligne);
    document.getElementById("bouton-sauvegarder").addEventListener("click", sauvegarder);
    document.getElementById("bouton-creer-nouvelle-facture").addEventListener("click", creer_nouvelle_facture);
}());