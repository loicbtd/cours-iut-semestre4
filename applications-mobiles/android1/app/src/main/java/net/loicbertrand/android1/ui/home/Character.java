package net.loicbertrand.android1.ui.home;

public class Character {
    int uid;
    String firstName;
    String familyname;
    String weburl;
    float latitude;
    float longitude;
    String bmppath;

    public Character(String firstName, String familyname, String weburl, float latitude, float longitude, String bmppath) {
        this.firstName = firstName;
        this.familyname = familyname;
        this.weburl = weburl;
        this.latitude = latitude;
        this.longitude = longitude;
        this.bmppath = bmppath;
    }

    public Character(int uid, String firstName, String familyname, String weburl, float latitude, float longitude, String bmppath) {
        this.uid = uid;
        this.firstName = firstName;
        this.familyname = familyname;
        this.weburl = weburl;
        this.latitude = latitude;
        this.longitude = longitude;
        this.bmppath = bmppath;
    }

    public int getUid() {
        return uid;
    }

    public String getFirstName() {
        return firstName;
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

    public String getBmppath() {
        return bmppath;
    }

    public void setUid(int uid) {
        this.uid = uid;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setFamilyname(String familyname) {
        this.familyname = familyname;
    }

    public void setWeburl(String weburl) {
        this.weburl = weburl;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }

    public void setBmppath(String bmppath) {
        this.bmppath = bmppath;
    }
}
