DROP TABLE IF EXISTS contient;
DROP TABLE IF EXISTS commande;
DROP TABLE IF EXISTS service;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS carte_reduction;

CREATE TABLE carte_reduction(
    id_carte_reduction INT AUTO_INCREMENT,
    carte VARCHAR(25),
    remise FLOAT,
    PRIMARY KEY(id_carte_reduction)
)ENGINE=InnoDB DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci;

CREATE TABLE client(
    code INT AUTO_INCREMENT,
    civilite VARCHAR(25),
    nom VARCHAR(25),
    prenom VARCHAR(25),
    adresse VARCHAR(50),
    code_postal NUMERIC(5,0),
    ville VARCHAR(25),
    id_carte_reduction INT,
    PRIMARY KEY(code),
    FOREIGN KEY (id_carte_reduction)
        REFERENCES carte_reduction(id_carte_reduction)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci AUTO_INCREMENT=1000000;

CREATE TABLE service(
    code INT AUTO_INCREMENT,
    prestation VARCHAR(50),
    cout NUMERIC(10,2),
    PRIMARY KEY(code)
)ENGINE=InnoDB DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci AUTO_INCREMENT=450001;

CREATE TABLE commande(
    num_commande INT AUTO_INCREMENT,
    prix_total FLOAT,
    date_commande DATE,
    code_client INT,
    PRIMARY KEY (num_commande),
    FOREIGN KEY (code_client)
        REFERENCES client(code)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci;

CREATE TABLE contient(
    num_commande INT,
    code_produit INT,
    quantite INT,
    FOREIGN KEY (num_commande)
        REFERENCES commande(num_commande)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (code_produit)
        REFERENCES service(code)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci;

INSERT INTO carte_reduction (carte, remise) VALUES('verte', 10);
INSERT INTO carte_reduction (carte, remise) VALUES('bleue', 25);
INSERT INTO carte_reduction (carte, remise) VALUES('orange', 34);
INSERT INTO carte_reduction (carte, remise) VALUES('rouge', 50);

INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Monsieur', 'BERTIN', 'Theophile', '12 rue des pres', 90000, 'Belfort', 1);
INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Monsieur', 'BISCHOFFE', 'Maxime', '7 rue de la madeleine', 90150, 'Denney', 3);
INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Madame', 'BITSCH', 'Magali', '8 rue des pervenches', 90400, 'Anjoutey', 2);
INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Madame', 'BRISWALTER', 'Melody', '12 rue des moulinets', 90180, 'Banvillard', 2);
INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Monsieur', 'CONCOLATOR', 'Florian', '7 rue des vergers', 90450, 'Bavilliers', 1);
INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Madame', 'FICHTER', 'Cecile', '9 rue de la moselle', 90100, 'Delle', 4);
INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Madame', 'FURSTER', 'Eline', '12 rue des feuilles', 90000, 'Belfort', 2);
INSERT INTO client (civilite, nom, prenom, adresse, code_postal, ville, id_carte_reduction) VALUES('Madame', 'JACQUOT', 'Sophie', '25 rue du piton', 90150, 'Etueffont', 4);

INSERT INTO service (prestation, cout) VALUES('raquettes', 3.00);
INSERT INTO service (prestation, cout) VALUES('batons par paires', 3.50);
INSERT INTO service (prestation, cout) VALUES('ski paraboliques', 3.25);
INSERT INTO service (prestation, cout) VALUES('ski de fond', 4.50);
INSERT INTO service (prestation, cout) VALUES('skating', 6.30);
INSERT INTO service (prestation, cout) VALUES('surf', 7.50);
INSERT INTO service (prestation, cout) VALUES('equipement pro combi', 7.00);