from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('tmr_app/login_page.html')
    context = {'IM GAY!'}
    return render(request, 'tmr_app/login_page.html')