package net.loicbertrand.android1.ui.credits;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class CreditsViewModel extends ViewModel {

    private MutableLiveData<String> mText;

    public CreditsViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("Credits: IUT BM, LP SIL, TeProW 2016");
    }

    public LiveData<String> getText() {
        return mText;
    }
}