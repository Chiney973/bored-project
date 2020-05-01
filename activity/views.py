from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})


def add_activity(request):
    return render(request, "add-activity.html", {})
