from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .forms import EmailForm
from django.http import HttpResponseBadRequest #for the bad request error.
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

            # Check if the email matches the pattern
            if re.match(email_pattern, email):  # Email is valid, print it to the terminal
                # Proceed with your logic if needed
                print(f"Entered email: {email}")
                #save the email to the database
                Email.objects.create(email=email)
                return HttpResponseBadRequest(f"Entered email: {email}")
            else:
                print("Unexpected error: Invalid email format.")
                return HttpResponseBadRequest("Unexpected error: Invalid email format.")
    else:
        form = EmailForm()
    
    return render(request, 'email.html', {'form': form})