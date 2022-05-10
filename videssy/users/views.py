"""Authentication views are listed here, any changes you make will affect
the authentication."""
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from vlog.models import Video
from .models import UserFollowing

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login as logthemin, logout as logthemout
from .forms import UserRegisterForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

User = get_user_model()


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                logthemin(request, user)
                messages.success(request, 'Logged in')
                return redirect('home')
            else:
                messages.success(request, 'Authentication error')
                return redirect('login')
        else:
            return render(request, 'login.html', {})
    else:
        return redirect('home')

def logout(request):
    if request.user.is_authenticated:
        logthemout(request)
        messages.success(request, 'Logged out')
        return redirect('home')
    else:
        messages.success(request, 'You can\'t log out if you are not logged in')
        return redirect('login')

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(uploader=User.objects.get(username=self.kwargs['username']))
        try:
            context['following'] = UserFollowing.objects.get(user__username=self.kwargs['username'], following_user=self.request.user)
        except ObjectDoesNotExist:
            context['following'] = None
        return context

user_detail_view = UserDetailView.as_view()

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Account created successfully, you may now log in!'
    template_name = 'register.html'

def subscribe(request, username):
    try:
        connection = UserFollowing.objects.get(user=get_object_or_404(User, username=username), following_user=request.user)
    except ObjectDoesNotExist:
        connection = None

    if connection is None:
        UserFollowing.objects.create(user=get_object_or_404(User, username=username), following_user=request.user)
    else:
        connection.delete()
    return redirect('detail', username)
