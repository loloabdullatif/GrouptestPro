from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from gradapplication.models import Farm,PublicPlace, User,FarmBooking
from django.db.models import Subquery

# Create your views here.
def farms(request):
    myfarms = User.objects.all().values() #البيانات الجاية من db
    template = loader.get_template('index.html')
    context = {
    'myfarms': myfarms, #dictionary #البيانات بحد ذاتها
    }
    return HttpResponse(template.render(context, request)) 

# def farms(request):
#     data = FarmBooking.objects.select_related('farmbooking__farmId').values('userId', 'farmbooking__farmId__name' )
#     # Pass the data to the template or do further processing
#     return render(request, 'index.html', {'data': data})