'''from celery import task
from django.core.mail import send_mail
from .models import Course
from django.conf import settings

@task
def course_created(course_id, course_email, course_user):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Course.objects.get(id=course_id)
    subject = 'Запись на курс: {} в школе Виктории Горбачевой'.format(order.title)
    message = 'Дорогой {},\n\nВы успешно записались на курс {}. В ближайшее время с Вами свяжется наш специалист'.format(course_user, order.title)

    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [course_email])
    return mail_sent



'''