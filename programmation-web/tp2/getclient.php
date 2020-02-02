<?php

define('BDD_hote','vpsloic.loicbertrand.net');
define('BDD_port','3310');
define('BDD_base_de_donnees','programmation_web_tp2');
define('BDD_usager','iut');
define('BDD_mot_de_passe','password');

const SQL_RECUPERER_INFORMATIONS_CLIENT = "
    SELECT civilite, mon, prenom, adresse, code_postal, ville, carte_reduction.etiquette
    FROM client
    INNER JOIN carte_reduction ON client.id_carte_reduction = carte_reduction.id_carte_reduction   
    WHERE client.code = ?
";

$connection = new PDO(
    "mysql:host=" . BDD_hote . ";port=" . BDD_port . ";dbname=" . BDD_base_de_donnees,
    BDD_usager,
    BDD_mot_de_passe);

$statement = $connection->prepare(SQL_RECUPERER_INFORMATIONS_CLIENT);
$statement->execute([$_GET['code']]);
while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
    $arr[] = $row;
    echo($row);
}

//$connection->exec("set names utf8");

// pour récupérer le résultat des requêtes SELECT sous la forme d'un tableau associatif
//$connection->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE,PDO::FETCH_ASSOC);

// pour afficher les erreurs
//$connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);