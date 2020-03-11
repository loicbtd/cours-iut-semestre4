package com.iutbm.example.iutbm.couchot.meetit_1;

import android.Manifest;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.LocationListener;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.iutbm.example.iutbm.couchot.meetit_1.donnees.BaseDeDonnees;
import com.iutbm.example.iutbm.couchot.meetit_1.donnees.CharacterDAO;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link MyMapFragment.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link MyMapFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class MyMapFragment extends Fragment implements OnMapReadyCallback, GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener, LocationListener, GoogleMap.OnMarkerClickListener {
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    private String mParam1;
    private String mParam2;

    private Location mLastLocation;
    private boolean mRequestingLocationUpdates;
    private LocationRequest mLocationRequest;
    private float radius;

    private List<Character> characterList = new ArrayList<>();
    private CharacterDAO characterDAO;
    private GoogleMap googleMap;

    private OnFragmentInteractionListener mListener;

    private GoogleApiClient mGoogleApiClient = null;

    private BroadcastReceiver restaurantBR;

    static int REQUEST_LOCATION = 1;

    public MyMapFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment MyMapFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static MyMapFragment newInstance(String param1, String param2) {
        MyMapFragment fragment = new MyMapFragment();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }


        if (mGoogleApiClient == null) {
            mGoogleApiClient = new GoogleApiClient.Builder(getActivity())
                    .addConnectionCallbacks(this)
                    .addOnConnectionFailedListener(this)
                    .addApi(LocationServices.API)
                    .build();
        }

        this.restaurantBR = new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                Toast.makeText(context, intent.getStringExtra(getResources().getString(R.string.key_best_restaurant_name_value)), Toast.LENGTH_SHORT).show();
            }
        };

    }

    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_my_map, container, false);
        SupportMapFragment mapFragment =
                (SupportMapFragment)
                        getChildFragmentManager().findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);


        BaseDeDonnees.getInstance(getContext());
        characterDAO = CharacterDAO.getInstance();

        characterList = characterDAO.recupererListeCharacter(getContext());

        return root;
    }


    // TODO: Rename method, update argument and hook method into UI event
    public void onButtonPressed(Uri uri) {
        if (mListener != null) {
            mListener.onFragmentInteraction(uri);
        }
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof OnFragmentInteractionListener) {
            mListener = (OnFragmentInteractionListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mListener = null;
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        this.googleMap = googleMap;
        LatLng belfort = new LatLng(47.6397, 6.8638);
        googleMap.moveCamera(CameraUpdateFactory.newLatLng(belfort));
        googleMap.moveCamera(CameraUpdateFactory.zoomTo(10));
    }

    @Override
    public void onStart() {
        super.onStart();
        mGoogleApiClient.connect();
    }

    @Override
    public void onStop() {
        super.onStop();
        mGoogleApiClient.disconnect();
    }


    @Override
    public void onConnected(@Nullable Bundle bundle) {
        if (ActivityCompat.checkSelfPermission(getActivity(), Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            requestLocationPermission();
        } else {
            mLastLocation = LocationServices.FusedLocationApi.getLastLocation(mGoogleApiClient);
            if (mLastLocation != null) {
                String lats = "" + mLastLocation.getLatitude();
                String longs = "" + mLastLocation.getLongitude();


//                TODO: TOAST
//                Toast.makeText(getActivity(), lats + " " + longs, Toast.LENGTH_LONG).show();
            }



            //            TODO: BROADCAST
            BestRestaurantAsyncTask bestRestaurantAsyncTask = new BestRestaurantAsyncTask(getContext(), new LatLng(mLastLocation.getLatitude(), mLastLocation.getLongitude()));
            bestRestaurantAsyncTask.execute();

        }

        if (mRequestingLocationUpdates){
            startLocationUpdates();
        }
        else {
            stopLocationUpdates();
        }
    }

    private void requestLocationPermission(){
        ActivityCompat.requestPermissions(
                getActivity(),
                new String[]{Manifest.permission.ACCESS_FINE_LOCATION},
                REQUEST_LOCATION);
    }

    private void setLocationParameters(){

        SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(getActivity());

        this.mRequestingLocationUpdates = sharedPreferences.getBoolean(getResources().getString(R.string.key_location_switch), false);

        this.mLocationRequest = LocationRequest.create().setInterval(Long.parseLong(sharedPreferences.getString(getResources().getString(R.string.key_search_delay), "0")));

        this.radius = Float.parseFloat(sharedPreferences.getString(getResources().getString(R.string.key_search_radius), "0")) / 1000;
    }



    @Override
    public void onConnectionSuspended(int i) {

    }

    @Override
    public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {

    }

    @Override
    public void onLocationChanged(Location location) {

        characterList = characterDAO.recupererListeCharacter(getContext());
        if (location != null){

            this.mLastLocation = location;
            googleMap.clear();

            float opacity;
            // afficher à proximité
            for (Character character : characterList) {
                if (character.getLatitude() < (float) location.getLatitude() + radius && character.getLongitude() < (float) location.getLongitude() + radius){

//                    TODO: TOAST A PROXIMITE
//                    Toast.makeText(getContext(), character.getFirstname()+" est à proximité !", Toast.LENGTH_SHORT).show();

                    opacity = 1;
                }
                else {
                    opacity = 0.5f;
                }

                MarkerOptions markerOptions = new MarkerOptions();
                markerOptions.alpha(opacity);
                markerOptions.position(new LatLng(character.getLatitude(), character.getLongitude())).title(character.getFirstname());
                markerOptions.title(character.getFirstname() + " " + character.getFamilyname());
                markerOptions.snippet(character.getWeburl());
                googleMap.setOnMarkerClickListener(this);
                googleMap.addMarker(markerOptions);
            }
        }
    }

    @Override
    public void onResume() {
        super.onResume();
        setLocationParameters();
        if (mGoogleApiClient.isConnected()){
            if (mRequestingLocationUpdates) {
                startLocationUpdates();
            } else {
                stopLocationUpdates();
            }
        }
        Objects.requireNonNull(getContext()).registerReceiver(restaurantBR, new IntentFilter(getResources().getString(R.string.key_restaurant_intent)));
    }



    protected void startLocationUpdates() {
        if (ActivityCompat.checkSelfPermission(getActivity(), Manifest.permission.ACCESS_FINE_LOCATION)
                != PackageManager.PERMISSION_GRANTED) {
            requestLocationPermission();
        } else {
            LocationServices.FusedLocationApi.requestLocationUpdates(
                    mGoogleApiClient, mLocationRequest, this);
        }
    }
    protected void stopLocationUpdates() {
        LocationServices.FusedLocationApi.removeLocationUpdates(
                mGoogleApiClient, this);
    }

    @Override
    public void onPause() {
        super.onPause();
        stopLocationUpdates();
        Objects.requireNonNull(getContext()).unregisterReceiver(restaurantBR);
    }

    @Override
    public boolean onMarkerClick(Marker marker) {
        Uri uriUrl = Uri.parse(marker.getSnippet());
        Intent launchBrowser = new Intent(Intent.ACTION_VIEW, uriUrl);
        startActivity(launchBrowser);
        return false;
    }


    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * <p>
     * See the Android Training lesson <a href=
     * "http://developer.android.com/training/basics/fragments/communicating.html"
     * >Communicating with Other Fragments</a> for more information.
     */
    public interface OnFragmentInteractionListener {
        // TODO: Update argument type and name
        void onFragmentInteraction(Uri uri);
    }
}
