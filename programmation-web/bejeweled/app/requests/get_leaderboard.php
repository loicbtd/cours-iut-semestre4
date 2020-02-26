<?php

require_once("./env.php");

const SQL_LISTER_LEADERBOARD = "
    SELECT id_leaderboard, username, score 
    FROM leaderboard
";

$connection = new PDO(
    "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_DATABASE,
    DB_USER,
    DB_PASSWORD);

$statement = $connection->prepare(SQL_LISTER_LEADERBOARD);
$statement->execute();

$tableau = array();
while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
    array_push($tableau, $row);
}
echo(json_encode($tableau));
