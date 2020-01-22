package com.iutbm.example.iutbm.couchot.meetit_1;

import android.graphics.Bitmap;

import java.net.URL;

/**
 * Created by couchot on 21/11/16.
 */

public class Character {
    private String firstname;
    private String familyname ;
    private URL weburl;
    private float latitude ;
    private float longitude ;
    private Bitmap bmp;

    public Character(String firstname, String familyname, URL weburl, float latitude, float longitude) {
        this.firstname = firstname;
        this.familyname = familyname;
        this.weburl = weburl;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public String getFirstname() {
        return firstname;
    }

    public String getFamilyname() {
        return familyname;
    }
    public URL getWeburl() {
        return weburl;
    }

    public float getLatitude() {
        return latitude;
    }

    public float getLongitude() {
        return longitude;
    }

    public Bitmap getBmp() {
        return bmp;
    }

}