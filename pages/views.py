from django.shortcuts import render

from submissions.models import Submission


def home(request):
    context = {}

    context['submissions'] = Submission.objects.all().order_by('-rating')[:5]

    return render(request, 'pages/home.html', context)
