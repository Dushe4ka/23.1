from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"\n\nИмя - {name}\n"
              f"Телефон - {phone}\n"
              f"Сообщение - {message}\n\n")

    return render(request, 'contacts.html')

# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'err.html', context)