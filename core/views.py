from django.shortcuts import render, redirect
from .forms import DynamicForm
from .models import FormData

def form_view(request):
    if request.method == "POST":
        # Получаем все поля name
        inputs = request.POST.getlist("name")
        data = {"names": inputs}
        FormData.objects.create(data=data)
        return redirect("list")  # после сохранения перенаправляем на список

    form = DynamicForm()
    return render(request, "core/form.html", {"form": form})


def list_view(request):
    items = FormData.objects.all()
    return render(request, "core/list.html", {"items": items})