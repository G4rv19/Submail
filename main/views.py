import re #regex
from django.shortcuts import render
from .forms import EmailForm
from django.http import HttpResponseBadRequest #for the bad request error.

def tasklist(request):
    return render(request, 'home.html')

def email_view(request):
    if request.method == 'POST': # if the request from is post
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'] #the email from the form in html by user
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" #regex code of email verification

            # Check if the email matches the pattern
            if re.match(email_pattern, email):
                # Email is valid, print it to the terminal
                print(f"Entered email: {email}")
                # Proceed with your logic if needed
                return HttpResponseBadRequest(f"Entered email: {email}")
            else:
                # Email is not valid, print an error to the terminal
                print("Unexpected error: Invalid email format.")
                # Return an HTTP 400 Bad Request response with an error message
                return HttpResponseBadRequest("Unexpected error: Invalid email format.")

    else:
        form = EmailForm()
    
    return render(request, 'your_template.html', {'form': form})