from django.shortcuts import render
from .models import Guitar

# Create your views here.
def index_view(request):
    guitars = Guitar.objects.all()
    return render(request, "index.html", {"guitars":guitars})

def detail_view(request):
    guitar = Guitar.objects.get(id=id)
    return render(request, "detail.html", {'guiter':guitar})