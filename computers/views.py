from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views.decorators.http import require_http_methods

from .models import Computer


# Create your views here.
@require_http_methods(["GET"])
def home(request: HttpRequest) -> HttpResponse:
    computers = Computer.objects.all()
    return render(request, 'computers/home.html', {'computer_list': computers})


@require_http_methods(["GET"])
def detail(request: HttpRequest, computer_id: int) -> HttpResponse:
    try:
        computer = get_object_or_404(Computer, pk=computer_id)
    except(KeyError, Computer.DoesNotExist):
        # Redisplay homepage
        return render(request, 'computers/home.html', {
            'error_message': "Please choose a exist computer and see its detail",
        })
    else:
        return render(request, 'computers/detail.html', {'computer': computer})

