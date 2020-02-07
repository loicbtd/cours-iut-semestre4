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

$tableau = array();
while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
    array_push($tableau, $row);
}
echo(json_encode($tableau));