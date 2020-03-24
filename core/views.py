from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import View
# Create your views here.
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from .models import Profile, Review
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, ReviewForm
from django.contrib import messages
from django.template import RequestContext



class FormCoreView(View):

    def get(self, request):
       return render(request, 'core/form.html')


def main(request):
    reviews = Review.objects.filter(active=True)
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            # Assign the current post to the comment
            new_review.name = request.user
            # Save the comment to the database
            new_review.save()

    if request.user.is_authenticated:
        review_entries = Review.objects.filter(name=request.user)
        if len(review_entries) == 0:
            review_entries = None
    else: review_entries = 1

    return render(request, 'core/main.html', {'reviews': reviews,
                                              'review_entries': review_entries})


@login_required
def dashboard(request):
    Profile_list = Profile.objects.get(user=request.user)
    context_dict = {'profile': Profile_list}
    return render(request, 'account/dashboard.html', context_dict)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно изменен')
            return render(request,
                          'account/edit.html',
                          {'user_form': user_form,
                           'profile_form': profile_form})
        else:
            messages.error(request, 'Ошибка изменения профиля')
            return render(request,
                          'account/edit.html',
                          {'user_form': user_form,
                           'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        try:
            unique_name = User.objects.get(username=request.POST['username'])
        except Exception:
            unique_name = False

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
        elif unique_name:
            messages.error(request, 'Ошибка! Пользователь с таким логином уже существует!')
        elif request.POST['password'] != request.POST['password2']:
            messages.error(request, 'Ошибка! Пароль и подтверждение пароля не совпадают!')
        else: messages.error(request, 'Ошибка! Указан неверный Email!')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def handler404(request, exception):
    context = RequestContext(request)
    err_code = 404
    response = render_to_response('core/404.html', {"code": err_code}, context)
    response.status_code = 404
    return response