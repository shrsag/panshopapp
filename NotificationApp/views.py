from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Recipient
from django.conf import settings
from smtplib import SMTPServerDisconnected
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages 

def send_notification(request, subject, message):
    try:
        if recipients := Recipient.objects.values_list('email', flat=True):
            from_email = settings.EMAIL_HOST_USER
            recipient_list = list(recipients)
            formatted_message = f"""
            <html>
                <body>
                    <p>Hello,</p>
                    <p><b>{message}</b></p>
                    <p>Thank you,</p>
                    <p>Shridhar Patil</p>
                </body>
            </html>
            """
            send_mail(subject, formatted_message, from_email, recipient_list, html_message=formatted_message)
        else:
            messages.success(request, "Please add receiver's email.")  # Fixed typo here
    except SMTPServerDisconnected:
        print("SMTP connection was unexpectedly closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

@login_required(login_url='login')
def home(request):
    request.session['first_visit'] = 'first_visit' not in request.session
    return render(request, 'index.html', {'first_visit': request.session['first_visit']})

@login_required
def open_notification(request):
    if request.session.get('shop_open', False):
        return render(request, 'index.html', {'error_message': 'Shop is already open, email already sent.'})
    
    send_notification(request,"Opened", "SHRIDHAR has opened the shop. Feel free to visit now!")
    request.session['shop_open'] = True
    request.session.modified = True
    return render(request, 'index.html', {'success_message': 'Shop is now opened, and notification has been sent.'})

@login_required
def close_notification(request):
    send_notification(request,"Closed", "SHRIDHAR has closed the shop. We will notify you once the shop is reopened.")
    request.session['shop_open'] = False
    request.session.modified = True
    return render(request, 'index.html', {'success_message': 'Shop is now closed, and notification has been sent.'})

@login_required
def add_email_page(request):
    return render(request, 'add_email.html')

@login_required
def add_email_database(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()

        if not email:
            return HttpResponse("Email is required!", status=400)

        recipient, created = Recipient.objects.get_or_create(email=email, defaults={"name": name})

        if created:
            return redirect('home')  # Redirect to home page after adding email
        else:
            return HttpResponse("Email already exists!", status=409)

    return HttpResponse("Invalid request method!", status=405)

def login_view(request):
    if request.method != "POST":
        return render(request, 'login.html')
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is None:
        return render(request, 'login.html', {
            'error_message': 'Invalid username or password.'
        })

    login(request, user)
    # Restore session state (like 'shop_open') after login
    if 'shop_open' in request.session:
        shop_open = request.session.get('shop_open')
        request.session['shop_open'] = shop_open
        request.session.modified = True
    return redirect('home')  # Redirect to the homepage after successful login


def logout_view(request):
    shop_open = request.session.get('shop_open', False)

    # Log the user out
    logout(request)

    # Restore session state
    request.session['shop_open'] = shop_open
    request.session.modified = True
    
    return redirect('login')


def about(request):
    return render(request, 'about.html')  
