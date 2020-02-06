from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime


def landing_page_ZNOtask(request):
    # hello = ("Hello")
    # return HttpResponse("Hello")

    return render(
        request,
        "ZNOtask.html",
        context={
            "Hello": "hello",
            "now": datetime.now()
        },
    )
