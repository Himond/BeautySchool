from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.core.validators import RegexValidator, MaxLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
telephone = RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_list_by_subject',
                       args=[self.slug])

class Course(models.Model):

    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    start = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='courses/%Y/%m/%d', blank=True, default='course.jpg')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail',
                       args=[self.id, self.slug])



class CourseEntry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField(validators=[telephone, MaxLengthValidator])
    course = models.ForeignKey(Course, related_name='courses_entry', on_delete=models.CASCADE)
    comments = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return 'Запись на курс № {}'.format(self.id)