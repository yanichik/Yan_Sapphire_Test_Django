from django.shortcuts import render

from django.contrib.auth import authenticate

from submissions.models import Submission


def home(request):
    context = {}
    # print("authenticate", authenticate)
    myUser = authenticate(username="yanichik", password="russia20")
    print("myUser", myUser)

    context["submissions"] = Submission.objects.all().order_by("-rating")[:10]

    return render(request, "pages/home.html", context)
