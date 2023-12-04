from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Login'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация прошла успешно'
    title = 'Registration'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    title = 'Profile'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
