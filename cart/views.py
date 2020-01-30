from django.shortcuts import render, get_object_or_404
from pages.models import Detail
def cart(request):
    cartlist = Detail.objects.all()
    return render(request, 'cart.html')



def checkout(request):

    return render(request, 'checkout.html')

