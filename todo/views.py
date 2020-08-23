from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_todo_list(requset):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(requset, 'todo/todo_list.html', context)


def add_item(requset):
    if requset.method == "POST":
        form = ItemForm(requset.POST)
        if form.is_valid:
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'from': form
    }
    return render(requset, 'todo/add_item.html', context)


def edit_item(requset, item_id):
    item = get_object_or_404(Item, id=item_id)
    if requset.method == "POST":
        form = ItemForm(requset.POST, instance=item)
        if form.is_valid:
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'from': form
    }
    return render(requset, "todo/edit_item.html", context)


def toggle_item(requset, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(requset, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
