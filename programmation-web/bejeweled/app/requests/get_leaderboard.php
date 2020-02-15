<?php

require_once("./env.php");

const SQL_LISTER_LEADERBOARD = "
    SELECT id_leaderboard, username, score 
    FROM leaderboard
    ORDER BY score DESC
";

$connection = new PDO(
    "mysql:host=" . BDD_hote . ";port=" . BDD_port . ";dbname=" . BDD_base_de_donnees,
    BDD_usager,
    BDD_mot_de_passe);

$statement = $connection->prepare(SQL_LISTER_LEADERBOARD);
$statement->execute();

$tableau = array();
while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
    array_push($tableau, $row);
}
echo(json_encode($tableau));
