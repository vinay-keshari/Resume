from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from castapp.forms import ProfileCreateForm


def ProfileCreateView(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
        print(request.user)
        return render(request, 'profile_create.html', {'profile_create_form': form})
