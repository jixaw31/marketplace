import time

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from base.forms import ItemForm
from .models import Item, Category, ConversationMessage
from .forms import ConversationMessageForm


# Create your views here.

def item_detail(request, pk):
    item = get_object_or_404(Item, id=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=pk)[:3]
    conversation_messages = ConversationMessage.objects.filter(item=item)
    form = ConversationMessageForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ConversationMessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.item = item
                message.sent_by = request.user
                message.save()
                messages.success(request, 'message added')

    return render(request, 'item_detail.html',
                  {'item': item,
                   'form': form,
                   'related_items': related_items,
                   'conversation_messages': conversation_messages,
                   })


@login_required(login_url='base:log-in')
def editItem(request, pk):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=Item.objects.get(id=pk))
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, 'Item edited')
            return redirect('item:item-detail', item.id)
    else:
        form = ItemForm(instance=Item.objects.get(id=pk))
    return render(request, 'edit_item.html', {'form': form})


@login_required(login_url='base:log-in')
def deleteItem(request, pk):
    # item = Item.objects.get(id=pk)
    item = get_object_or_404(Item, id=pk, created_by=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'item deleted')
        return redirect('base:index')
    return render(request, 'delete_item.html')
