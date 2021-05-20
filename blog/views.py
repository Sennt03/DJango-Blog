from django.shortcuts import redirect, render, get_object_or_404
from django.urls.conf import path
from .forms import FormCategory, FormEntry
from .models import Category, Article
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    articulos = Article.objects.order_by('-id').all()
    
    return render(request, 'entradas/index.html', {
        'articulos': articulos
    })

@login_required(login_url='login')
def add_categoria(request):

    form = FormCategory()

    if request.method == 'POST':
        form = FormCategory(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            notvalidate = Category.objects.filter(name=name)
            
            if notvalidate:
                messages.error(request, f"Categoria '{name}' ya existe")
            else:
                category = Category(name=name)
                
                category.save()
                messages.success(request, f"Categoria '{name}' creada correctamente")
                
        else:
            messages.error(request, 'Error al crear la categoria')

    return render(request, 'categorias/add.html', {
        'form': form
    })


@login_required(login_url='login')
def add_entrada(request):
    form = FormEntry()

    if request.method == 'POST':
        form = FormEntry(request.POST, request.FILES)
        if form.is_valid():
            
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            
            messages.success(request, 'Entrada creada correctamente')
        else:
            messages.error(request, 'No se ha guardado la entrada')
        
    return render(request, 'entradas/add.html', {
        'form': form
    })


@login_required(login_url='login')
def delete_article(request, id):
    confirm = False
    article = False
    try:
        article = Article.objects.raw('SELECT * FROM blog_article WHERE id = %s AND user_id = %s', [id, request.user.id])[0]
        confirm = True
    except:
        confirm = False
    
    if confirm:
        article.delete()
        messages.success(request, 'Articulo borrado correctamente')

    else:
        messages.success(request, 'Ocurrio un error al borrar el articulo')

    return redirect('index')


@login_required(login_url='login')
def edit_article(request, id):

    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        form = FormEntry(request.POST,instance=article)
        if form.is_valid():
            form.save() #aqui estas guardando diractamente el formulario en la base de datos
            messages.success(request, 'Entrada editada correctamente')
    else:
        form = FormEntry(instance=article)

    return render(request, 'entradas/edit.html', {
        'form': form,
        'article': article
    })


def category(request, id):

    confirm = False
    articulos = Article.objects.order_by('-id').filter(category_id=id)
    try:
        category = Category.objects.get(id=id)
        confirm = True
    except:
        confirm = False

    if confirm:    
        return render(request, 'entradas/categorys.html', {
            'articulos': articulos,
            'category': category
        })
    else:
        return redirect('index')


def user(request, id):

    confirm = False
    articulos = Article.objects.order_by('-id').filter(user_id=id)
    try:
        usuario = User.objects.get(id=id)
        confirm = True
    except:
        confirm = False
    if confirm:
        return render(request, 'entradas/user.html', {
            'articulos': articulos,
            'usuario': usuario
        })
    else:
        return redirect('index')