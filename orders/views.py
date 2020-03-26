from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount

            """Отправка письма без асинхронности"""

            try:
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])


                subject = 'Заказ №. {}'.format(order.id)
                message = 'Дорогой {},\n\nВы успешно записались на услугу в салоне красоты БэкСтейдж.\
                                            Ваш идентификатор заказа {}. В ближайшее время с Вами свяжется наш специалист'.format(
                    order.first_name,
                    order.id)
                send_mail(subject,
                         message,
                         settings.EMAIL_HOST_USER,
                         [order.email])
                    # очистка корзины
                cart.clear()

                return render(request, 'orders/order/created.html',
                              {'order': order})

            except Exception:
                messages.success(request,
                                 'Электронной почты {} не существует. Проверьте правильность введенных данных'.format(
                                     order.email))

                Order.objects.filter(id=order.id).delete()
                return render(request, 'orders/order/create.html',
                              {'cart': cart, 'form': form})

            # запуск асинхронной задачи
            #order_created.delay(order.id)

        else:
            messages.error(request, 'Ошибка! Указан неверный Email!')
    else:
        if request.user.is_authenticated:
            form = OrderCreateForm(instance=request.user)
        else:
            form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})