from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Company,Client

def home(request):

    latest_company_list = Company.objects.order_by('-created_at')[:5]
    #template = loader.get_template('compnies/home.html')
    context = {
        'latest_company_list': latest_company_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'compnies/home.html', context)

def client(request, company):

    company_obj = Company.objects.get(id=company)
    client_list = Client.objects.filter(company=company_obj)
    #template = loader.get_template('compnies/home.html')
    context = {
        'latest_Client_list': client_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'compnies/details.html', context)
    #return HttpResponse("This is Client for this Company %s." % name)    
# Create your views here.
