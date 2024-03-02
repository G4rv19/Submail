from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import EmailForm
from .models import Email
import re

def tasklist(request):
    return render(request, 'home.html')

def email_view(request):
    # Form submission handling
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

            # Check if the email matches the pattern
            if re.match(email_pattern, email):
                # Check if the email already exists in the database
                if Email.objects.filter(email=email).exists():
                    print("Email already exists")
                    return render(request, 'exists.html')
                else:
                    print("Saved to db")
                    # Save the email to the database
                    Email.objects.create(email=email)
                    return render(request, 'email.html', {'form': form})
            else:
                print("Unexpected error: Invalid email format.")
                return HttpResponseBadRequest("Unexpected error: Invalid email format.")
    else:
        form = EmailForm()

    # Render the form when the page is first loaded or on form validation failure
    return render(request, 'email.html', {'form': form})
