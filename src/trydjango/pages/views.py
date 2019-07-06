from django.http import HttpResponse
from django.shortcuts import render
#from django.views.generic import TemplateView

# Create your views here.
def home_view(request, *args,**kwargs):
    print(request.user)
    print(args,kwargs)
    #return HttpResponse("<h1>Hello World</h1>")
    return render (request, "home.html", {})

def contact_view(request, *args,**kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
    return render (request, "contact.html", {})
def about_view(request, *args,**kwargs):
    #return HttpResponse("<h1>About Page</h1>")
    return render (request, "about.html", {})
def mingle_view(request, *args,**kwargs):
    #return HttpResponse("<h1>Mingling Page</h1>")
    return render (request, "mingle.html", {})
def test_view(request,*args,**kwargs):
    return render (request,"test.html",{})


#class IndPageView(TemplateView):
#    template_name = "ind.html"


#class AboutPageView(TemplateView):
#    template_name = "about.html"
