from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )[0:3]

    context = {"item": item, "related_items": related_items}

    return render(request, "item/detail.html", context)


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()

    context = {"form": form, "title": "New Item"}
    return render(request, "item/form.html", context)
