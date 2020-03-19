package com.iutbm.example.iutbm.couchot.meetit_1;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class ChraracterListAdapter extends RecyclerView.Adapter<CharacterViewHolder> {

    private List<Character> characterList;
    private Context context;

    public ChraracterListAdapter(List<Character> characterList, Context context) {
        this.context = context;
        this.characterList = characterList;
        setHasStableIds(true);
    }

    @Override
    public long getItemId(int position) {
        return super.getItemId(position);
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
        holder.latitudeView.setText(String.format("%s", teacher.getLatitude()));
        holder.longitudeView.setText(String.format("%s", teacher.getLongitude()));
        Drawable drawable = context.getResources().getDrawable(
                context.getResources().getIdentifier(
                        teacher.getBmp(), "drawable", context.getPackageName()));

        Bitmap bitmap = ((BitmapDrawable) drawable).getBitmap();
        Drawable adjusted_drawable = new BitmapDrawable(
                context.getResources(),
                Bitmap.createScaledBitmap(bitmap, 150, 150, true)
        );
        holder.pictureView.setImageDrawable(adjusted_drawable);
    }

    @Override
    public int getItemCount() {
        return characterList.size();
    }
}