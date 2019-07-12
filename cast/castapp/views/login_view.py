from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout

from castapp.forms import login_page_form
from castapp.models import profile, AcademicDetail

def login(request):
    if request.method == 'POST':
        form = login_page_form(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data.get('email') or form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
            except AttributeError:
                return HttpResponse('BAD REQUEST')
        user = authenticate(username=username, password=password)
        if user:
            user_data = get_object_or_404(get_user_model(), username=username)
            details = profile.objects.select_related('academic_data').filter(email=user_data.email)
            if details:
                details = details[0]
                return render(request, 'profile_page.html',{"profile_data":details})
            else:
                return render(request,'error.html')
            
        else:
            render(request, 'login-page.html')
    else:
        form = login_page_form()

    return render(request, 'login-page.html', {'form': form})

