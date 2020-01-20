package net.loicbertrand.android1.ui.home;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProviders;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import net.loicbertrand.android1.R;

import java.util.ArrayList;

public class HomeFragment extends Fragment {

    private HomeViewModel homeViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        homeViewModel = ViewModelProviders.of(this).get(HomeViewModel.class);

        View root = inflater.inflate(R.layout.fragment_home, container, false);

        RecyclerView recyclerView = root.findViewById(R.id.fragment_home_recycler_view_character);
        recyclerView.setLayoutManager(new LinearLayoutManager(root.getContext()));

        ArrayList<Character> listCharacter = new ArrayList<>();
        Character character;
        for (int i = 0; i < 10; i++) {
            character = new Character(
              i,
              "firstname "+i,
              "familyname "+i,
              "weburl "+i,
                    (float) Math.random(),
                    (float) Math.random(),
              "bmppath "+i
            );
            listCharacter.add(character);
        }

        recyclerView.setAdapter(new MyAdapter(listCharacter));

        return root;
    }
}