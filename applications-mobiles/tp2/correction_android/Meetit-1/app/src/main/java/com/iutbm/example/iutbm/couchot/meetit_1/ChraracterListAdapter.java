package com.iutbm.example.iutbm.couchot.meetit_1;

import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.List;

public class ChraracterListAdapter extends RecyclerView.Adapter<CharacterViewHolder> {

    private List<Character> characterList;

    public ChraracterListAdapter(List<Character> characterList) {
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
        holder.firstNameView.setText(teacher.getFirstname());
        holder.familyNameView.setText(teacher.getFamilyname());
        holder.latitudeView.setText("" + teacher.getLatitude());
        holder.longitudeView.setText("" + teacher.getLongitude());
    }

    @Override
    public int getItemCount() {
        return characterList.size();
    }
}