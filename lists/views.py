from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})
    # items = Item.objects.filter(list=list_)
    # return render(request, 'list.html', {
    #     'items': items,
    # })


def new_list(request):
    new_item_text = request.POST['item_text']
    list_ = List.objects.create()
    item = Item.objects.create(text=new_item_text, list=list_)
    try:
        item.full_clean()
    except ValidationError:
        list_.delete()
        error = 'You cannot have an empty list item'
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % (list_.id,))


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_id,))
