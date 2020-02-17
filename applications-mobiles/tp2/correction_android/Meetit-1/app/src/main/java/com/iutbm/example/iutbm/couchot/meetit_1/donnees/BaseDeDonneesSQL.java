package com.iutbm.example.iutbm.couchot.meetit_1.donnees;

public interface BaseDeDonneesSQL {
    String SQL_CREER_TABLE_CHARACTER = "CREATE TABLE character(" +
            "id_character INTEGER PRIMARY KEY, " +
            "firstname TEXT, " +
            "familyname TEXT, " +
            "weburl TEXT," +
            "latitude REAL," +
            "longitude REAL," +
            "bmp TEXT" +
            ")";
    String SQL_DETRUIRE_TABLE_CHARACTER = "DROP TABLE IF EXISTS character";
    String SQL_DECRIRE_TABLE_CHARACTER = "PRAGMA table_info(character);";
}