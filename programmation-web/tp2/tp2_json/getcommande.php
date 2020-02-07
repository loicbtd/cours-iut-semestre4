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

$tableau = array();
while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
    array_push($tableau, $row);
}
echo(json_encode($tableau));
