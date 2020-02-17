DROP TABLE IF EXISTS leaderboard;

CREATE TABLE leaderboard(
    id_leaderboard INT AUTO_INCREMENT,
    username VARCHAR(25),
    score FLOAT,
    PRIMARY KEY (id_leaderboard)
)ENGINE=InnoDB DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci;