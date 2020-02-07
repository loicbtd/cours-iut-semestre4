LOAD DATA LOCAL INFILE './mockdata/carte_reduction.csv' INTO TABLE carte_reduction FIELDS TERMINATED BY ';' (carte,remise);
LOAD DATA LOCAL INFILE './mockdata/client.csv' INTO TABLE client FIELDS TERMINATED BY ';' (civilite,nom,prenom,adresse,code_postal,ville,id_carte_reduction);
LOAD DATA LOCAL INFILE './mockdata/service.csv' INTO TABLE service FIELDS TERMINATED BY ';' (prestation,cout);