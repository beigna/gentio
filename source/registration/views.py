
from django.shortcuts import render, get_object_or_404, redirect

from registration.forms import RegistrationForm

def register(request):
    if request.method == 'GET':
        form = RegistrationForm()

    elif request.method == 'POST':
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            # Create User
            # Create ActivationProfile
            return redirect(reverse('registration_pending'))

    return render(request, 'registration/register.html',
        {
            'form': form,
        }
    )

def pending(request):
    return render(request, 'registration/pending.html',
        {},
    )
