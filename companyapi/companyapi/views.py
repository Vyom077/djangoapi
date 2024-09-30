from django.http import HttpResponse

def home_page(request):
    print("Home Page request")
    return HttpResponse("This is home page")


