package net.loicbertrand.android1.ui.home;

import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import net.loicbertrand.android1.R;

public class CharacterViewHolder extends RecyclerView.ViewHolder{

    public TextView firstnameView;
    public TextView familynameView;
    public TextView latitudeView;
    public TextView longitudeView;
    public ImageView pictureImageView;


    public CharacterViewHolder(View itemView) {
        super(itemView);
        this.firstnameView = (TextView) itemView.findViewById(R.id.text_view_character_first_name);
        this.familynameView = (TextView) itemView.findViewById(R.id.text_view_character_family_name);
        this.latitudeView = (TextView) itemView.findViewById(R.id.text_view_character_latitude);
        this.longitudeView = (TextView) itemView.findViewById(R.id.text_view_character_longitude);
        this.pictureImageView = (ImageView) itemView.findViewById(R.id.image_view_character_pitcture);
    }
}