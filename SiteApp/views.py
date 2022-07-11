from django.shortcuts import render
from SiteApp.autoadd import adding
from SiteApp.models import Site

# Create your views here.
def home(request):
    site=Site.objects.all()
    if site.count()!=11:
        adding()
    data=[]
    for  s in site:
        s.get_mixed_data(context=data)
    context={
        'tags':data
    }    
       
    return render(request,'index.html',context)

def get_news(request,name):
    site=Site.objects.get(name=name)
    print(site.get_data())
    context={
        'tags':site.get_data()
    }
    return render(request,'index.html',context)