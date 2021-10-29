from django.shortcuts import render
from .models import Setting
from Product_app.models import Product
# Create your views here.
def HomePage(request):
    context = {}

    if Setting.objects.exists():
        setting = Setting.objects.get(id=1)
        context={'setting':setting}
    if Product.objects.exists():
        prod_slide_img = Product.objects.all().order_by('id')[:2]
        context={'setting':setting,'prod_slide_img':prod_slide_img}
        
    return render(request, 'ecommerceApp/home.html',context)