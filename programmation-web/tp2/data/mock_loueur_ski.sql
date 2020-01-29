\COPY marque(nom, couleur_logo, slogan, date_creation) FROM './mockdata/marque.csv' DELIMITER ';' CSV;
\COPY voiture(modele, couleur, puissance, annee, id_marque) FROM './mockdata/voiture.csv' DELIMITER ';' CSV;


