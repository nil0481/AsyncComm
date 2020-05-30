
from django.shortcuts import render
from . models import Product, Orders
from math import ceil
# Create your views here.
from django.http import HttpResponse

def index(request):
    allProds = []
    catprod = Product.objects.values('category',
                                     'id')  # list of dictionaries [ {'category': 'home appliances', 'id': 13},...]
    # print(catprod)
    cats = {item['category'] for item in catprod}  # dictionary of {'Electrical', 'watch'....}
    # print (cats)

    for cat in cats:
        prod = Product.objects.filter(category=cat)  # category wise List of products
        # print(prod)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        # print(allProds)
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")


def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')  # '' is default value
        amount = request.POST.get('amount', '')  # '' is default value
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + "  " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders(items_json=items_json, name=name, email=email, phone=phone,
                       address=address, city=city, state=state, zip_code=zip_code,
                       amount=amount)  # name(database)=name(variable here)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
