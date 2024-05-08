from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user_form.html'
    extra_context = {
        'title': 'Registration',
        'btn_text': 'Sign up',
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    next_page = '/employees/'


class Logout(LogoutView):
    next_page = reverse_lazy('main')
