package com.iutbm.example.iutbm.couchot.meetit_1;

import android.graphics.Bitmap;

import java.net.URL;

public class Character {

    public static final String CLE_ID_CHARACTER= "id_character";
    public static final String CLE_FIRSTNAME = "firstname";
    public static final String CLE_FAMILYNAME = "familyname";
    public static final String CLE_WEBURL = "weburl";
    public static final String CLE_LATITUDE = "latitude";
    public static final String CLE_LONGITUDE = "longitude";
    public static final String CLE_BMP = "bmp";

    private int idCharacter;
    private String firstname;
    private String familyname ;
    private String weburl;
    private float latitude ;
    private float longitude ;
    private String bmp;

    public Character(int idCharacter, String firstname, String familyname, String weburl, float latitude, float longitude, String bmp) {
        this.idCharacter = idCharacter;
        this.firstname = firstname;
        this.familyname = familyname;
        this.weburl = weburl;
        this.latitude = latitude;
        this.longitude = longitude;
        this.bmp = bmp;
    }

    public Character(int idCharacter, String firstname, String familyname, String weburl, float latitude, float longitude) {
        this.idCharacter = idCharacter;
        this.firstname = firstname;
        this.familyname = familyname;
        this.weburl = weburl;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public Character(String firstname, String familyname, String weburl, float latitude, float longitude) {
        this.firstname = firstname;
        this.familyname = familyname;
        this.weburl = weburl;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public int getIdCharacter() {
        return idCharacter;
    }

    public String getFirstname() {
        return firstname;
    }

    public String getFamilyname() {
        return familyname;
    }

    public String getWeburl() {
        return weburl;
    }

    public float getLatitude() {
        return latitude;
    }

    public float getLongitude() {
        return longitude;
    }

    public String getBmp() {
        return bmp;
    }
}