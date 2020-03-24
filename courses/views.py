from django.shortcuts import render, get_object_or_404
from .models import Subject, Course
from .forms import EntryForm
from django.contrib import messages

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


