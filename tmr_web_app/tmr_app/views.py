from django.shortcuts import render
from django.template import loader
from tmr_app.models import Units

# Create your views here.
def index(request):
    template = loader.get_template('tmr_app/login_page.html')
    context = Units.objects.all()
    print(context)
    return render(request, 'tmr_app/login_page.html', {'content':context})