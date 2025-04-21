from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    judul = 'about'
    isi = 'Ini bagian isinya'
    data = {
        'title' : judul,
        'isi' : isi,
    }

    return render(request,'profil/index.html',data)