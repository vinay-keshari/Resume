from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from castapp.forms import registration_form, ProfileCreateForm


def register_user(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')
            except AttributeError:
                return HttpResponse('BAD REQUEST')
        try:
            user=get_user_model().objects.create_user(username, password=password, email=email)
            user.save()
            register_form = ProfileCreateForm()
            return render(request, 'profile_create.html', {'profile_create_form': register_form})
        except:
            return HttpResponse('<h1>Unable to create</h1>')
    if request.method == 'GET':
        form = registration_form()
        return render(request, 'registration_page.html', {'registration_form': form})
