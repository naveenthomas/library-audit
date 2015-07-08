from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from .models import Book, Count, Shelf
from django.views.generic import View,ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse,reverse_lazy

# Create your views here.
from .forms import ShelfCountForm,ShelfForm


class ShelfList(ListView):
    model = Shelf
    fields = ['row_1']
    template_name = 'shelf_list.html'


class ShelfCreate(CreateView):
    model = Shelf
    fields = ['shelf_no','row_1','row_2','row_3','book_file']
    template_name = 'shelf_create.html'
    success_url = reverse_lazy('shelf-list')
    

class ShelfUpdate(UpdateView):
    model = Shelf
    fields = ['row_1','row_2','row_3','book_file']
    template_name = 'shelf_create.html'
    success_url = reverse_lazy('shelf-list')

    
class ShelfDelete(DeleteView):
    model = Shelf
    template_name = 'shelf_confirm_delete.html'
    success_url = reverse_lazy('shelf-list')
    
