package net.loicbertrand.android1.ui.home;

import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class MyAdapter extends RecyclerView.Adapter<CharacterViewHolder> {

    private ArrayList<Character> dataSource;

    public MyAdapter(ArrayList<Character> dataArgs){
        dataSource = dataArgs;
    }

    @Override
    public CharacterViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

        View firstnameView = new TextView(parent.getContext());
        View familynameView = new TextView(parent.getContext());
        View latitudeView = new TextView(parent.getContext());
        View longitudeView = new TextView(parent.getContext());
//        ImageView = new ImageView(parent.getContext());

        CharacterViewHolder viewHolder = new CharacterViewHolder(firstnameView, familynameView, latitudeView, longitudeView);

        return viewHolder;
    }

    @Override
    public void onBindViewHolder(CharacterViewHolder holder, int position) {
        holder.firstnameTextView.setText(dataSource.get(position).getFirstName());
        holder.familynameTextView.setText(dataSource.get(position).getFamilyname());
        holder.latitudeTextView.setText(String.format("%s", dataSource.get(position).getLatitude()));
        holder.longitudeTextView.setText(String.format("%s", dataSource.get(position).getLongitude()));
//        holder.pictureImageView TODO: manage picture view
    }

    @Override
    public int getItemCount() {
        return dataSource.size();
    }
}