package net.loicbertrand.android1.ui.home;

import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class CharacterViewHolder extends RecyclerView.ViewHolder{

    public TextView firstnameTextView;
    public TextView familynameTextView;
    public TextView latitudeTextView;
    public TextView longitudeTextView;
    public ImageView pictureImageView;


    public CharacterViewHolder(@NonNull View firstnameTextView,@NonNull View familynameTextView,@NonNull View latitudeTextView,@NonNull TextView longitudeTextView) {
        super(itemView);
        this.firstnameTextView = (TextView) firstnameTextView;
        this.familynameTextView = (TextView) familynameTextView;
        this.latitudeTextView = (TextView) latitudeTextView;
        this.longitudeTextView = (TextView) longitudeTextView;
//        this.pictureImageView = (ImageView) pictureImageView;
    }
}