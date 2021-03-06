<?php

require_once("./env.php");

const SQL_LISTER_CONTIENT_PAR_ID_CLIENT= "
    SELECT num_commande, code_produit, quantite FROM contient;
";

$connection = new PDO(
    "mysql:host=" . BDD_hote . ";port=" . BDD_port . ";dbname=" . BDD_base_de_donnees,
    BDD_usager,
    BDD_mot_de_passe);

$statement = $connection->prepare(SQL_LISTER_CONTIENT_PAR_ID_CLIENT);
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