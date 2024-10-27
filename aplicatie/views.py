from django.shortcuts import render, redirect
from .models import Produs, session


# Create your views here.
def shopping_list(request):
    produse = session.query(Produs).all()
    return render(request, 'pages/shopping_list.html', {'produse': produse})


def adauga(request):
    if request.method == 'POST':
        nume_produs = request.POST.get('nume')
        produs_nou = Produs(nume=nume_produs)
        session.add(produs_nou)
        session.commit()
        return redirect('/')
    return render(request, 'pages/adauga.html')


def sterge(request, produs_id):
    produs = session.query(Produs).get(produs_id)
    if produs:
        session.delete(produs)
        session.commit()
    return redirect('/')


def cumpara(request, produs_id):
    produs = session.query(Produs).get(produs_id)
    if produs:
        produs.cumparat = True
        session.commit()
        return redirect('/')
    return redirect('/')