

from django.shortcuts import render
from .models import Text
from .forms import TextForm

def home(request):
    form =TextForm()
    return render(request, 'base/home.html', {'form':form})

# Create your views here.
