<?php

require_once("./env.php");

if (! isset($_POST['id']) ) exit();
if (! isset($_POST['username']) ) exit();
if (! isset($_POST['score']) ) exit();



$connection = new PDO(
    "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_DATABASE,
    DB_USER,
    DB_PASSWORD);

const SQL_UPDATE_LEADERBOARD = "
    UPDATE leaderboard
    SET username = ?, score = ?  
    WHERE id_leaderboard = ?;
";


//echo($_POST['id']." ".$_POST['username']." ".$_POST['score']);

$statement = $connection->prepare(SQL_UPDATE_LEADERBOARD);
$statement->execute([$_POST['username'], $_POST['score'], $_POST['id']]);
print_r($statement->errorInfo());

