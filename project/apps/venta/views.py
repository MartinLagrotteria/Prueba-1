from django.shortcuts import render
from libros.models import Autor, Libro, Editor
from .forms import LibroForm
def index(request):
    return render(request, "venta/index.html")



def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})
