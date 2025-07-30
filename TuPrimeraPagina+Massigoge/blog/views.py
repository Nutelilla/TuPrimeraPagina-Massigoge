from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def agregar_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario_autor.html', {'form': form})

def agregar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario_categoria.html', {'form': form})

def agregar_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/formulario_post.html', {'form': form})

def buscar_post(request):
    resultado = None
    if request.method == 'POST':
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultado = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPostForm()
    return render(request, 'blog/buscar_post.html', {'form': form, 'resultado': resultado})