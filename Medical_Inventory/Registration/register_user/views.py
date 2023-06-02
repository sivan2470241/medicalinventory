from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import User
from datetime import datetime,timedelta
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.contrib import messages
# Create your views here.

#--------Registration View----

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.registration_id = get_random_string(length=10)
            # user.registration_id = generate_token(user)  # Generate a unique registration ID
            user.save()
            # Send email to the registered candidate
            send_registration_email(request,user)
            # Perform additional processing or redirect to a success page
            # return redirect('success') 
            messages.success(request, 'Registration successful!') 
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

#--------Registration View----


#---------Email Sending Function View----    

def send_registration_email(request,user):
    current_site = get_current_site(request)
    registration_link = f"http://{current_site.domain}/update/{user.registration_id}/"
    subject = "Registration Confirmation and Content Update"
    html_message = render_to_string('email_template.html', {'registration_link': registration_link,'user':user})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER  # Sender Email Address
    to_email = user.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

#---------Email Sending Function View----    



#--------Update View----------------

def content_update_view(request,registration_id):
    try:
        user = User.objects.get(registration_id=registration_id)
        print(registration_id)
        # current_time = datetime.now()
        current_time = timezone.now()

        seven_days_ago = current_time - timedelta(days=7)
        if user.updated_at is not None and user.updated_at < seven_days_ago:
            # Registration ID expired, handle accordingly   
            # return redirect('expired_registration')
                return HttpResponse("expirred")
 
        if request.method == 'POST':
            form = RegistrationForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                # Perform additional processing or redirect to a success page
                # return redirect('success')  # Replace 'success' with the desired URL
                return HttpResponse("success")
        else:
            form = RegistrationForm(instance=user)
    except User.DoesNotExist:
        # Handle invalid or expired registration ID
        # return redirect('invalid_registration')
        return HttpResponse('invalid_registration')

    return render(request, 'content_update.html', {'form': form})

#--------Update View----------------

def success(request):
    return render(request,'index.html')