package net.loicbertrand.android1.ui.home;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProviders;
import androidx.recyclerview.widget.DefaultItemAnimator;
import androidx.recyclerview.widget.DividerItemDecoration;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import net.loicbertrand.android1.R;

import java.util.ArrayList;
import java.util.List;

public class HomeFragment extends Fragment {

    private HomeViewModel homeViewModel;

    private List<Character> characterList;
    private RecyclerView recyclerView;

    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        homeViewModel = ViewModelProviders.of(this).get(HomeViewModel.class);

        View view = inflater.inflate(R.layout.fragment_home, container, false);

        recyclerView = view.findViewById(R.id.fragment_home_recycler_view_character);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity().getApplicationContext()));
        recyclerView.setItemAnimator(new DefaultItemAnimator());
        recyclerView.addItemDecoration(new DividerItemDecoration(getContext(), LinearLayoutManager.VERTICAL));

        prepareCharacterData();

        recyclerView.setAdapter(new CharacterListAdapter(characterList));

        return view;
    }

    private void prepareCharacterData() {
        characterList = new ArrayList<>();
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
            characterList.add(character);
        }
    }
}