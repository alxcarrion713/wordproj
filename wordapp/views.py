from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    
    if 'counter' not in request.session:
        request.session['counter']=1
    else:
        request.session['counter']+=1
    randword= get_random_string(length=14)
    context = {
        'randwordContext': randword
    }
    return render(request, "index.html",context)

def resetgame(request):
    del request.session['counter']
    return redirect('/random_word')


