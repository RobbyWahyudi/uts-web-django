from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def products(request):
    template = loader.get_template("product.html")
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())