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

$reponse = new DOMDocument('1.0', 'utf-8');
$element_clients = $reponse->createElement('clients');
$reponse->appendChild($element_clients);

while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {

    $tmp_element_client = $reponse->createElement('client');
    $element_clients->appendChild($tmp_element_client);

    $keys = array_keys($row);

    foreach ($keys as $key){
        $tmp_property = $reponse->createElement($key, $row[$key]);
        $tmp_element_client->appendChild($tmp_property);
    }
}
echo($reponse->saveXML());
