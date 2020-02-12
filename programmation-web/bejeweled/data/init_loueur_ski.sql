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


