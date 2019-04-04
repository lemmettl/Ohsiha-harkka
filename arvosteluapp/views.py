from django.shortcuts import render, redirect
from .models import Arvostelu
from .forms import ArvosteluForm

def list_arvostelut(request):
    arvostelut = Arvostelu.objects.all()
    return render(request, 'home.html', {'arvostelut':arvostelut})

def create_arvostelu(request):
    form = ArvosteluForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_arvostelut')
    return render(request, 'arvostelu-form.html', {'form':form})

def update_arvostelu(request, id):
    arvostelu = Arvostelu.objects.get(id=id)
    form = ArvosteluForm(request.POST or None, Instance=arvostelu)

    if form.is_valid():
        form.save()
        return redirect('list_arvostelut')
    return render(request, 'arvostelu-form.html', {'form':form, 'arvostelu':arvostelu})

def delete_arvostelu(request, id):
    arvostelu = Arvostelu.objects.get(id=id)
    
    if request.method == 'POST':
        arvostelu.delete()
        return redirect('list_arvostelut')
    return render(request, 'arvostelu-deleted.html', {'arvostelu':arvostelu})