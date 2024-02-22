from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .forms import EmailForm
from .models import Email
from django.shortcuts import render
import re


def tasklist(request):
    return render(request, 'home.html')

def email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            if re.match(email_pattern, email):
                # Email is valid, save it to the database
                Email.objects.create(email=email)
                return HttpResponse(f"Entered email: {email} (Saved to the database)")
            else:
                print("Unexpected error: Invalid email format.")
                return HttpResponseBadRequest("Unexpected error: Invalid email format.")
    else:
        form = EmailForm()
        print("Get request only")
 
    return render(request, 'email.html', {'form': form})