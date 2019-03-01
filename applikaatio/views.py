from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate   #autentikointi
from django.contrib.auth.forms import UserCreationForm  #autentikointi

def HomePageView(request):
    return render(request, 'base.html', {})

#Seuraavaksi määritellään mitä tapahtuu, kun uusi käyttäjä täyttää kirjautumislomakkeen

def signup(request):
    if request.method == 'POST':        #Jos käyttäjä tulee sivulle ensimmäistä kertaa
        form = UserCreationForm(request.POST)
        if form.is_valid():         #tarkistetaan onko formi hväksyttävä tallennettavaksi
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

