package com.iutbm.example.iutbm.couchot.meetit_1;

import android.content.Context;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v4.app.Fragment;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.DividerItemDecoration;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link MyDataFragment.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link MyDataFragment#newInstance} factory method to
 * create an instance of this fragment.
 */



public class MyDataFragment extends Fragment {
    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    private SharedPreferences sharedPref;
    private TextView tv_loc_enabled_out = null;
    private View root = null;

    private List<Character> characterList = new ArrayList<>();
    private RecyclerView recyclerView;
//    private ChraracterListAdapter mAdapter;


    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    private OnFragmentInteractionListener mListener;

    public MyDataFragment() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment MyDataFragment.
     */
    // TODO: Rename and change types and number of parameters
    public static MyDataFragment newInstance(String param1, String param2) {
        MyDataFragment fragment = new MyDataFragment();
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





    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        // Inflate the layout for this fragment
        root = inflater.inflate(R.layout.fragment_my_data, container, false);
        recyclerView = root.findViewById(R.id.character_recycler_view);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity().getApplicationContext()));
        recyclerView.setItemAnimator(new DefaultItemAnimator());
        recyclerView.addItemDecoration(new DividerItemDecoration(getContext(),LinearLayoutManager.VERTICAL));
        recyclerView.setAdapter(new ChraracterListAdapter(characterList));

        prepareCharacterData();
        return root;
    }

    public void updateUI(){
        sharedPref = PreferenceManager.getDefaultSharedPreferences(getActivity());

        Boolean locationEnabled = sharedPref.getBoolean(getResources().getString(R.string.key_location_switch), false);
        String isLocationEnable = ": ";
        isLocationEnable += locationEnabled ? "True" : "False";
        tv_loc_enabled_out = (TextView) root.findViewById(R.id.text_location_switch_out);
        tv_loc_enabled_out.setText(isLocationEnable);

        String search_delay = sharedPref.getString(getResources().getString(R.string.key_search_radius), "NC");
        TextView text_view_search_delay = (TextView) root.findViewById(R.id.text_search_delay_out);
        text_view_search_delay.setText(String.valueOf(search_delay));

        String radius = sharedPref.getString(getResources().getString(R.string.key_search_radius), "NC");
        TextView text_view_search_radius = (TextView) root.findViewById(R.id.text_search_radius_out);
        text_view_search_radius.setText(String.valueOf(radius));
    }


    // TODO: Rename method, update argument and hook method into UI event
    public void onButtonPressed(Uri uri) {
        if (mListener != null) {
            mListener.onFragmentInteraction(uri);
        }
    }

    @Override
    public void onResume(){
        super.onResume();
        updateUI();
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

    public void prepareCharacterData() {
        Character c1, c2, c3;
        try {
            c1 = new Character("Jean-François", "Couchot", new URL("http://members.femto-st.fr/jf-couchot/fr"), 47.642900f, 6.840027f);
            c2 = new Character("Raphaël", "Couturier", new URL("http://members.femto-st.fr/raphael-couturier/fr"), 47.659518f, 6.813337f);
            c3 = new Character("Stéphane","Domas", new URL("http://info.iut-bm.univ-fcomte.fr/staff/sdomas/"), 47.6387143f, 6.8370225f);
            characterList.add(c1);
            characterList.add(c2);
            characterList.add(c3);
        } catch (Exception e) {

        }
    }

}
