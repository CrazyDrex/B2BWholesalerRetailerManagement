from django.shortcuts import render
from listings.choices import price_choices, category_choices, state_choices 
from listings.models import Listing



# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'category_choices': category_choices,
    }
    # context ={
    #     "variable1" : "this is not sent",
    #      "variable2" : "abhishek is great"
    # } # context are list of variables show on templte.
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')

     
    # return HttpResponse("this is aboutpage")   

# def services(request):
#     return render(request, 'services.html')
#      # return HttpResponse("this is services page")  

# def contact(request):
#     return render(request, 'contact.html')
#     # return HttpResponse("this is contact page")                 