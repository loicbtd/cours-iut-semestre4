package com.iutbm.example.iutbm.couchot.meetit_1.donnees;

public interface CharacterSQL {
    String SQL_LISTER_CHARACTER = "SELECT * FROM character";
    String SQL_INSERER_CHARACTER = "INSERT INTO character(firstname, familyname, weburl, latitude, longitude, bmp) VALUES(?,?,?,?,?,?)";
    String SQL_MODIFIER_CHARACTER = "UPDATE character SET firstname = ?, familyname = ?, weburl = ?, latitude = ?, longitude = ? where id_character = ?";
//    String SQL_MODIFIER_CHARACTER = "UPDATE character SET firstname = ?, familyname = ?, weburl = ?, latitude = ?, longitude = ?, bmp = ? where id_character = ?";
}
