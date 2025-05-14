# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import EditProfileForm
from .models import Profile


@login_required
def user_detail(request, username: str):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'users/user_detail.html', dict(user=user, profile=profile))


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if (form := EditProfileForm(request.POST, request.FILES, instance=profile)).is_valid():
            form.save()
            messages.success(request, 'User profile has been successfully saved.')
            return redirect('users:user-detail', request.user.username)
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def leave(request):
    if not request.user.profile.is_teacher():
        user = User.objects.get(username=request.user)
        user.delete()
        messages.success(request, 'Good bye! Hope to see you soon.')
        return redirect('/')
    return HttpResponseForbidden('Prohibido')
