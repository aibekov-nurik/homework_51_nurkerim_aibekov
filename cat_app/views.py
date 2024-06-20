# cat_app/views.py
from django.shortcuts import render, redirect
from .models import Cat
from .forms import CatForm, ActionForm

def home(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            cat = form.save()
            return redirect('cat_info', cat_id=cat.id)
    else:
        form = CatForm()
    return render(request, 'home.html', {'form': form})

def cat_info(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            if action == 'feed':
                cat.feed()
            elif action == 'play':
                cat.play()
            elif action == 'sleep':
                cat.sleep()
            cat.save()
            return redirect('cat_info', cat_id=cat_id)
    else:
        form = ActionForm()
    return render(request, 'cat_info.html', {'cat': cat, 'form': form})
