from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ReviewStudio, Masters
from .forms import ReviewStudioForm
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    reviews = ReviewStudio.objects.filter(active=True)
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    masters = Masters.objects.filter(active=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if request.method == 'POST':
        if request.user.is_authenticated:
            review_form = ReviewStudioForm(data=request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                # Assign the current post to the comment
                new_review.name = request.user
                # Save the comment to the database
                new_review.save()

    if request.user.is_authenticated:
        review_entries = ReviewStudio.objects.filter(name=request.user)
        if len(review_entries) == 0:
            review_entries = None
    else: review_entries = 1

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form,
                   'reviews': reviews,
                   'review_entries': review_entries,
                   'masters': masters
                   })



def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,})