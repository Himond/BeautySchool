from django.urls import path, re_path
from django.contrib import auth
from django.urls import reverse_lazy
from blog import views

urlpatterns = [
    # templates views
    path('', views.PostListView.as_view(), name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]