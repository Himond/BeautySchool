from django.shortcuts import render, get_object_or_404
from .models import Subject, Course
from .forms import EntryForm
from django.contrib import messages
from .tasks import course_created
from django.core.mail import send_mail
from django.conf import settings

def course_list(request, subject_slug=None):
    subject = None
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    if subject_slug:
        subject = get_object_or_404(Subject, slug=subject_slug)
        courses = courses.filter(subject=subject)

    return render(request,
                  'courses/course/list.html',
                  {'subject': subject,
                   'subjects': subjects,
                   'courses': courses})



def course_detail(request, id, slug):
    course = get_object_or_404(Course,
                                id=id,
                                slug=slug)
    price_with_discount = course.price - (course.price/100)*course.discount
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            entry_form = entry_form.save(commit=False)
            entry_form.course = course
            entry_form.save()
            messages.success(request, 'Ваша заявка отправлена! Наш менеджер свяжется с вами в ближайшее время!')

            """Отправка письма без асинхронности"""
            order = Course.objects.get(id=entry_form.course.id)
            subject = 'Запись на курс: {} в школе Виктории Горбачевой'.format(order.title)
            message = 'Дорогой {},\n\nВы успешно записались на курс {}. В ближайшее время с Вами свяжется наш специалист'.format(
                entry_form.first_name, order.title)

            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                     [entry_form.email])

            """Отправка письма асинхронно"""
            #course_created.delay(entry_form.course.id, entry_form.email, entry_form.first_name)

            return render(request,
                          'courses/course/detail.html',
                          {'entry_form': entry_form,
                           'course': course,
                           'price_with_discount': price_with_discount
                           })
    else:
        if request.user.is_authenticated:
            entry_form = EntryForm(instance=request.user)
        else:
            entry_form = EntryForm
    return render(request, 'courses/course/detail.html', {'course': course,
                                                          'entry_form': entry_form,
                                                          'price_with_discount': price_with_discount
                                                          })


