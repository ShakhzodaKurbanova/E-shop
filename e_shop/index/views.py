from django.shortcuts import render, redirect
from .models import Product, Category, Cart
# Create your views here.


def home_page(request):
    # Получаем данные из бд
    products = Product.objects.all()
    categories = Category.objects.all()

    # Передаем данные на фронт
    context = {'products': products,
               'categories': categories}
    return render(request, 'home.html', context)


def get_exact_pr(request, pk):
    exact_product = Product.objects.get(id=pk)

    # Передаем данные на фронт
    context = {'product': exact_product}
    return render(request, 'product.html', context)


def get_exact_category(request, pk):
    exact_category = Category.objects.get(id=pk)
    products = Product.objects.filter(pr_category=exact_category)

    # Передаем данные на фронт
    context = {'products': products}
    return render(request, 'category.html', context)


def to_cart(request, pk):
    if request.method == 'POST':
        product = Product.objects.filter(id=pk)
        if product.pr_count >= int(request.POST.get('user_product_quantity')):
            Cart.objects.create(user_id=request.user.id,
                                user_product=product.pr_name,
                                user_product_quantty=int(request.POST.get
                                                         ('user_product_quantity'))).save()
            return redirect('/')


def get_user_cart(request):
    user_cart = Cart.objects.filter(user_id=request.user.id)
    # отправляем данные на фронт
    context = {'cart': user_cart}
    return render(request, 'cart.html', context)


def del_from_cart(request, pk):
    product_to_delete = Product.objects.filter(id=pk)
    Cart.objects.filter(user_id=request.user.id,
                        user_product=product_to_delete).delete()
    return redirect('/cart')
