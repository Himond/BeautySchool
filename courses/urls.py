from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    re_path(r'^(?P<subject_slug>[-\w]+)/$', views.course_list, name='course_list_by_subject'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.course_detail, name='course_detail'),
]