from django import forms
from libros.models import Autor, Libro, Editor

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion']
