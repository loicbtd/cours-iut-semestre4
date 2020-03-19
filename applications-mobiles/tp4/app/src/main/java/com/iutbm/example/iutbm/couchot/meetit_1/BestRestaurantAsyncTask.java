package com.iutbm.example.iutbm.couchot.meetit_1;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;

import com.google.android.gms.maps.model.LatLng;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class BestRestaurantAsyncTask extends AsyncTask {
    private Context mContext;
    private LatLng location;
    private LatLng latLngR = null;
    private String restauName = null;


    public BestRestaurantAsyncTask(Context mContext, LatLng location) {
        super();
        this.mContext = mContext;
        this.location = location;
    }

    @Override
    protected Object doInBackground(Object[] objects) {

        URL url;
        StringBuffer response = new StringBuffer();
        try {
            url = new URL("https://maps.googleapis.com/maps/api/place/nearbysearch/json?" +
                    "&location=" + location.latitude + "," + location.longitude +
                    "&radius=10000" +
                    "&type=restaurant" +
                    "&key=AIzaSyCfmj0zcWfYy0c7ihjPIwuVRjIVscwbj0I");
        } catch (MalformedURLException e) {
            throw new IllegalArgumentException("invalid url");
        }

        HttpURLConnection conn = null;
        try {
            conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(false);
            conn.setDoInput(true);
            conn.setUseCaches(false);
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8");

            // handle the response
            int status = conn.getResponseCode();
            if (status != 200) {
                throw new IOException("Post failed with error code " + status);
            } else {
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                String inputLine;
                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (conn != null) {
                conn.disconnect();
            }

            //Here is your json in string format
            String responseJSON = response.toString();

            interprete_json_file(responseJSON);
        }

        if (latLngR != null && restauName != null){
            Intent i = new Intent(mContext.getResources().getString(R.string.key_restaurant_intent));
            i.putExtra(mContext.getResources().getString(R.string.key_best_restaurant_name_value), restauName + " : " + latLngR.longitude + " " + latLngR.latitude);
            mContext.sendBroadcast(i);
        }

        return null;
    }

    private void interprete_json_file(String jsontext){
        try {
            JSONObject racine = new JSONObject(jsontext);
            JSONArray results = racine.getJSONArray("results");
            JSONObject res0 = results.getJSONObject(0);
            JSONObject geometry = res0.getJSONObject("geometry");
            JSONObject location = geometry.getJSONObject("location");
            double lat = location.getDouble("lat");
            double longi = location.getDouble("lng");
            this.latLngR = new LatLng(lat,longi);
            this.restauName = res0.getString("name");
        }catch (JSONException e) {
            e.printStackTrace();
        }
    }
}
