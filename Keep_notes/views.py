from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Notes_form
from .models import notes_storage


# Create your views here.
def create_notes(request):
    if request.method == "POST":
        form = Notes_form(request.POST)
        print(form)
        print(form)
        form.save()
        return redirect("create_notes")



    return render(request, "Create_notes.html")


def delete(request, Id):
    data = notes_storage.objects.get(Id=Id)
    data.delete()
    return redirect("watch")


def edit(request, id):
    field = notes_storage.objects.get(id=id)

    return render(request, "note/edit.html", {"field": field})


def update(request, Id):
    field_data = notes_storage.objects.get(Id=Id)
    edited_form = Notes_form(request.POST, instance=field_data)

    if edited_form.is_valid():
        edited_form.save()
        return redirect("watch")


def watch(request):
    model = notes_storage.objects.all()
    print(model)
    return render(request,'watch.html',{"model": model})


def bydefualt(request):
     return render(request,"navigation.html")
