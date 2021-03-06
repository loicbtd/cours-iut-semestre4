<?php

require_once("./env.php");

$donnees_brutes = $_POST['var'];

$donnees_commande = preg_split('/\|/', $donnees_brutes, -1)[0];
$donnees_contient = preg_split('/\|/', $donnees_brutes, -1)[1];
$donnees_contient = preg_split('/\;/', $donnees_contient, -1);

$prix_total = preg_split('/;/', $donnees_commande, -1)[0];
$date_commande = preg_split('/;/', $donnees_commande, -1)[1];
$date_commande = preg_split('/\//', $date_commande)[2]."-".preg_split('/\//', $date_commande)[1]."-".preg_split('/\//', $date_commande)[0];
$code_client = preg_split('/;/', $donnees_commande, -1)[2];
$contient = array();
foreach ($donnees_contient as $item){
    $code_produit = preg_split('/,/', $item, -1)[0];
    $quantite = preg_split('/,/', $item, -1)[1];
    array_push($contient, [$code_produit, $quantite]);
}

//echo("$prix_total: ".$prix_total."\n");
//echo("$date_commande: ".$date_commande."\n");
//echo("$code_client: ".$code_client."\n");

//for ($i=0; $i<sizeof($contient); $i++){
//    echo("produit ".$i.": code=".$contient[$i][0]." et quantite=".$contient[$i][1]."\n");
//}

$connection = new PDO(
    "mysql:host=" . BDD_hote . ";port=" . BDD_port . ";dbname=" . BDD_base_de_donnees,
    BDD_usager,
    BDD_mot_de_passe);

const SQL_INSERER_NOUVELLE_COMMANDE = "
    INSERT INTO commande(prix_total,date_commande,code_client) VALUES (?,?,?);
";

const SQL_INSERER_NOUVELLE_COMMANDE_AVEC_NUM_COMMANDE = "
    INSERT INTO commande(num_commande, prix_total,date_commande,code_client) VALUES (?,?,?,?);
";

const SQL_RECUPERER_ID_DERNIERE_COMMANDE = "
    SELECT max(num_commande) as num_commande FROM commande;
";

const SQL_INSERER_CONTIENT_COMMANDE = "
    INSERT INTO contient(num_commande,code_produit,quantite) VALUES (?,?,?);
";

const SQL_SUPPRIMER_COMMANDE = "
    DELETE FROM commande WHERE num_commande=?;
";

const SQL_SUPPRIMER_CONTIENT = "
    DELETE FROM contient WHERE num_commande=?;
";

if (isset($_POST['num_commande'])) {
    $num_commande = $_POST['num_commande'];
    echo("update order number; ".$num_commande);
    // si la commande existe, on la supprime
    $statement = $connection->prepare(SQL_SUPPRIMER_COMMANDE);
    $statement->execute([$num_commande]);

    $statement = $connection->prepare(SQL_SUPPRIMER_CONTIENT);
    $statement->execute([$num_commande]);
//    print_r($statement->errorInfo());

    $statement = $connection->prepare(SQL_INSERER_NOUVELLE_COMMANDE_AVEC_NUM_COMMANDE);
    $statement->execute([$num_commande, $prix_total, $date_commande, $code_client]);
//    print_r($statement->errorInfo());
}
else {
    $statement = $connection->prepare(SQL_INSERER_NOUVELLE_COMMANDE);
    $statement->execute([$prix_total, $date_commande, $code_client]);
//    print_r($statement->errorInfo());

    $statement = $connection->prepare(SQL_RECUPERER_ID_DERNIERE_COMMANDE);
    $statement->execute();
//    print_r($statement->errorInfo());
    $num_commande = $statement->fetch(PDO::FETCH_ASSOC)['num_commande'][0];

    echo("create order number; ".$num_commande);

}

foreach ($contient as $element) {
    $statement = $connection->prepare(SQL_INSERER_CONTIENT_COMMANDE);
    $statement->execute([$num_commande, $element[0], $element[1]]);
//    print_r($statement->errorInfo());
}
