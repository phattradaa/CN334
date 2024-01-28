from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def ecommerce_index_view(request):
    '''This function render index page of ecommerc views'''
    
    return HttpResponse('Welcome to 6410742099 Phattrada Mikota views')

def item_view(request, item_id):
    
    context_data = {
        "item_id" : item_id
    }
    
    return render(request,'index.html',context=context_data)

def home_page(request):
    
    return render(request,'homepage.html')

def category_page(request):
    
    return render(request,'category.html')

def product_page(request):
    
    return render(request,'product.html')

def checkout_page(request):
    
    return render(request,'checkout.html')

def contact_page(request):
    
    return render(request,'contact.html')
