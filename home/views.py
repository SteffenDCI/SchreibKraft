from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# deprecated by class-based view "HomeView"
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_content = {'today': datetime.today()}
    

# deprecated by class-based view "AuthorizedView"
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url= '/admin'
    
