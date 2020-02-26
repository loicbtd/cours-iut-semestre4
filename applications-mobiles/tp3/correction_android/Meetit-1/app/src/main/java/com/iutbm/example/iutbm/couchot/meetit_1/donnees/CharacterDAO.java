package com.iutbm.example.iutbm.couchot.meetit_1.donnees;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteStatement;

import com.iutbm.example.iutbm.couchot.meetit_1.Character;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class CharacterDAO implements CharacterSQL {

    private static CharacterDAO instance = null;
    protected List<Character> listeCharacter;

    private BaseDeDonnees accesseurBaseDeDonnees;

    public static CharacterDAO getInstance() {
        if (null == instance) {
            instance = new CharacterDAO();
        }
        return instance;
    }

    public CharacterDAO() {
        this.accesseurBaseDeDonnees = BaseDeDonnees.getInstance();
        listeCharacter = new ArrayList<>();
    }

    public List<Character> recupererListeCharacter(Context context) {
        Cursor curseur = accesseurBaseDeDonnees.getReadableDatabase()
                .rawQuery(SQL_LISTER_CHARACTER, null);
        this.listeCharacter.clear();

        Character character;

        int indexId_character = curseur.getColumnIndex(Character.CLE_ID_CHARACTER);
        int indexFirstname = curseur.getColumnIndex(Character.CLE_FIRSTNAME);
        int indexFamilyname = curseur.getColumnIndex(Character.CLE_FAMILYNAME);
        int indexWeburl = curseur.getColumnIndex(Character.CLE_WEBURL);
        int indexLatitude = curseur.getColumnIndex(Character.CLE_LATITUDE);
        int indexLongitude = curseur.getColumnIndex(Character.CLE_LONGITUDE);
        int indexBmp = curseur.getColumnIndex(Character.CLE_BMP);

        for (curseur.moveToFirst(); !curseur.isAfterLast(); curseur.moveToNext()) {
            int id_character = curseur.getInt(indexId_character);
            String firstname = curseur.getString(indexFirstname);
            String familyname = curseur.getString(indexFamilyname);
            URL weburl = null;
            try {
                weburl = new URL(curseur.getString(indexWeburl));
            } catch (MalformedURLException e) {
                e.printStackTrace();
            }
            float latitude = curseur.getFloat(indexLatitude);
            float longitude = curseur.getFloat(indexLongitude);
            String bmp = curseur.getString(indexBmp);
//            // TODO: remplacer "couturier" par bmp_id
//            Drawable drawable = context.getResources().getDrawable(context.getResources().getIdentifier("couturier", "drawable", context.getPackageName()));
//            Bitmap bmp = ((BitmapDrawable) drawable).getBitmap();
//
            character = new Character(id_character, firstname, familyname, weburl, latitude, longitude, bmp);
            this.listeCharacter.add(character);
        }
        return listeCharacter;
    }

    public void ajouterCharacter(Character character) {
        SQLiteDatabase sqLiteDatabase = accesseurBaseDeDonnees.getWritableDatabase();
        SQLiteStatement sqLiteStatement = sqLiteDatabase.compileStatement(SQL_INSERER_CHARACTER);
        sqLiteStatement.bindString(1, character.getFirstname());
        sqLiteStatement.bindString(2, character.getFamilyname());
        sqLiteStatement.bindString(3, character.getWeburl().toString());
        sqLiteStatement.bindDouble(4, character.getLatitude());
        sqLiteStatement.bindDouble(5, character.getLongitude());
        sqLiteStatement.bindString(6, character.getBmp());
        sqLiteStatement.execute();
    }

    public Character chercherCharacterParIdCharacter(int id_character) {
        for(Character characterRecherche : this.listeCharacter) {
            if(characterRecherche.getIdCharacter() == id_character) return characterRecherche;
        }
        return null;
    }

    public void modifierCharacter(Character character) {
        SQLiteDatabase sqLiteDatabase = accesseurBaseDeDonnees.getWritableDatabase();
        SQLiteStatement sqLiteStatement = sqLiteDatabase.compileStatement(SQL_MODIFIER_CHARACTER);
        sqLiteStatement.bindString(1, character.getFirstname());
        sqLiteStatement.bindString(2, character.getFamilyname());
        sqLiteStatement.bindString(3, character.getWeburl().toString());
        sqLiteStatement.bindDouble(4, character.getLatitude());
        sqLiteStatement.bindDouble(5, character.getLongitude());
        sqLiteStatement.bindString(6, character.getBmp());
        sqLiteStatement.execute();
    }
}
