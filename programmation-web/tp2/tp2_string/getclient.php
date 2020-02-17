<?php

require_once("./env.php");

const SQL_LISTER_CLIENTS = "
    SELECT code, civilite, nom, prenom, adresse, code_postal, ville, carte_reduction.carte, carte_reduction.remise
    FROM client
    INNER JOIN carte_reduction ON client.id_carte_reduction = carte_reduction.id_carte_reduction
";

$connection = new PDO(
    "mysql:host=" . BDD_hote . ";port=" . BDD_port . ";dbname=" . BDD_base_de_donnees,
    BDD_usager,
    BDD_mot_de_passe);

$statement = $connection->prepare(SQL_LISTER_LEADERBOARD);
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