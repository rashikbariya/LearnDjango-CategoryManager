# from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic
from django.shortcuts import redirect

from .models import Categories
from .forms import CategoryForm
# Create your views here.

#retrive all
def index(request):
    all_categories = Categories.objects.filter(is_active=True)
    context = {'all_categories': all_categories}
    return render(request, 'categories/index.html', context)

#retrive single category
def detail_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})

 #create   
def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'categories/add.html', {'form': form})

#update
def edit_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/edit.html', {'form': form})

#delete
def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('categories:index')




# class IndexView(generic.ListView):
#     template_name = 'categories/index.html'
#     context_object_name = 'all_categories'

#     def get_queryset(self):
#         """Return all categories."""
#         return Categories.objects.all()

# class DetailView(generic.DetailView):
#     model = Categories
#     template_name = 'categories/detail.html'