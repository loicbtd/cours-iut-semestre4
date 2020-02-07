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

$statement = $connection->prepare(SQL_LISTER_CLIENTS);
$statement->execute();

$reponse = new DOMDocument('1.0', 'utf-8');
$element_clients = $reponse->createElement('clients');
$reponse->appendChild($element_clients);

$tableau = array();
while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
    array_push($tableau, $row);
}
echo(json_encode($tableau));
