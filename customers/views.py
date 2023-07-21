from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

def index(request):
    context = {
        'title' : "maniverse Home",
    }
    return render(request, 'customer/index.html', context=context)


