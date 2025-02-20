from django.shortcuts import render,redirect
from .forms import MemberForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
'''def homepage(request):
    return HttpResponse('<h1>Biennvene mon boutique en ligne  </h1>')'''

def homepage(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Merci pour ton inscription!')
            print("✅ ")  
            
     
    else:
        form = MemberForm()

    return render(request, 'ecommerceapp/index.html', {'form': form})


def membreviews(request,memberid):
    return render(request,'ecommerceapp/memberviews.html', locals())