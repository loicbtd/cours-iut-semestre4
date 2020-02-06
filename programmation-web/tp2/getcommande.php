<?php

require_once("./env.php");

const SQL_LISTER_COMMANDES= "
    SELECT num_commande, prix_total, date_commande, code_client FROM commande;
";

$connection = new PDO(
    "mysql:host=" . BDD_hote . ";port=" . BDD_port . ";dbname=" . BDD_base_de_donnees,
    BDD_usager,
    BDD_mot_de_passe);

$statement = $connection->prepare(SQL_LISTER_COMMANDES);
$statement->execute();

$reponse = "";
while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
    foreach ($row as $cell){
        $reponse .= $cell.",";
    }
    $reponse = substr($reponse, 0, -1);
    $reponse .= "\n";
}

$reponse = substr($reponse, 0, -1);
echo($reponse);