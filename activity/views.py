from django.shortcuts import render


def random_activity(request):
    return render(request, "random-activity.html", {})


def add_activity(request):
    return render(request, "add-activity.html", {})
