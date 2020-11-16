from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
    iban_num = request.POST.get('iban')
    user = request.POST.get('user')
    #Account.objects.create(owner = user, iban = iban_num)
    return redirect('/')


@login_required
def homePageView(request):
    user = request.POST.get('user')
    owned_accs = Account.objects.filter(owner__first_name = user)
    return render(request, 'pages/index.html', {'accounts': owned_accs})
