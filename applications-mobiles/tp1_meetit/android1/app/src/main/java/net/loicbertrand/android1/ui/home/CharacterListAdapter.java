package net.loicbertrand.android1.ui.home;

import android.graphics.Bitmap;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.recyclerview.widget.RecyclerView;

import net.loicbertrand.android1.R;

import java.util.ArrayList;
import java.util.List;

public class CharacterListAdapter extends RecyclerView.Adapter<CharacterViewHolder> {

    private List<Character> characterList;

    public CharacterListAdapter(List<Character> characterList) {
        this.characterList = characterList;
    }

    @Override
    public CharacterViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext()).inflate(R.layout.fragment_character, parent, false);
        return new CharacterViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(CharacterViewHolder holder, int position) {

        Character teacher = characterList.get(position);
        holder.firstnameView.setText(teacher.getFirstName());
        holder.familynameView.setText(teacher.getFamilyname());
        holder.latitudeView.setText(String.format("%s", teacher.getLatitude()));
        holder.longitudeView.setText(String.format("%s", teacher.getLongitude()));
//        holder.pictureImageView.setImageBitmap(new Bitmap()); TODO: manage bitmap
    }

    @Override
    public int getItemCount() {
        return characterList.size();
    }
}