from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
#
#
# @login_required
# def dashboard(request):
#     return render(request,
#                   'account/dashboard.html',
#                   {'section': 'dashboard'})
#
#
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # set the chosen password
#             new_user.save()
#             return render(request, 'account/register_done.html',
#                           {'new_user': new_user})
#             # save the user object
#             new_user.save()
#             return render(request, 'account/register_done.html',
#                           {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'user_form': user_form})


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'