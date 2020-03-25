'''from celery import task
from django.core.mail import send_mail
from .models import Order
from django.conf import settings

@task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ №. {}'.format(order_id)
    message = 'Дорогой {},\n\nВы успешно записались на услугу в салоне красоты БэкСтейдж.\
                Ваш идентификатор заказа {}. В ближайшее время с Вами свяжется наш специалист'.format(order.first_name,
                                             order.id)

    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email])
    return mail_sent


'''