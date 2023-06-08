from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils import timezone
from .forms import RegistrationForm
import re
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Registration
from django.contrib.sites.shortcuts import get_current_site
from django.utils.crypto import get_random_string
from django.conf import settings
from datetime import datetime,timedelta
from django.utils import timezone
from django.contrib import messages

         

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            registration = form.save()
            registration.registration_id = get_random_string(length=10)
            registration.save()
           
            # Additional Validations
            name = registration.name
            email = registration.email
            mobile = registration.mobile
            photo = registration.photo
            resume = registration.resume

            # Name validation
            if not name.isalpha() or len(name) > 50:
                form.add_error('name', 'Invalid name. Only letters are allowed, and it should not exceed 50 characters.')
            
            

            # Mobile validation
            if not mobile.isdigit() or len(mobile) != 10:
                form.add_error('mobile', 'Invalid mobile number. It should be a 10-digit number.')

            # Photo validation
            if photo:
                if photo.size > 200 * 1024:  # 200KB in bytes
                    form.add_error('photo', 'The photo should not exceed 200KB in size.')
                if not photo.name.lower().endswith(('.jpg', '.jpeg')):
                    form.add_error('photo', 'Only JPG and JPEG formats are allowed for the photo.')

            # Resume validation
            if resume:
                if resume.size > 500 * 1024:  # 500KB in bytes
                    form.add_error('resume', 'The resume should not exceed 500KB in size.')
                if not resume.name.lower().endswith(('.pdf', '.doc', '.docx')):
                    form.add_error('resume', 'Only PDF, DOC, and DOCX formats are allowed for the resume.')

        

            # Save the registration
            send_update_link_email(request, registration)

            messages.success(request, 'Registration successful!')
            return redirect('success' )
            # Sending email
            
    else:

        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def send_update_link_email(request,registration):
    current_site = get_current_site(request)
    registration_link = f"http://{current_site.domain}/registration/update/{registration.registration_id}/"
    subject = "Registration Confirmation and Content Update"
    html_message = render_to_string('registration/email.html', {'registration_link': registration_link,'registration':registration})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER  # Sender Email Address
    to_email = registration.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


def content_update_view(request,registration_id):
    try:
        registration =Registration.objects.get(registration_id=registration_id)
        print(registration_id)
        # current_time = datetime.now()
        current_time = timezone.now()

        seven_days_ago = current_time - timedelta(days=7)
        if registration.updated_at is not None and registration.updated_at < seven_days_ago:
            # Registration ID expired, handle accordingly   
            # return redirect('expired_registration')
                return HttpResponse("expirred")
 
        if request.method == 'POST':
            form = RegistrationForm(request.POST, request.FILES, instance=registration)
            if form.is_valid():
                form.save()
                # Perform additional processing or redirect to a success page
                # return redirect('success')  # Replace 'success' with the desired URL
                return HttpResponse("success")
        else:
            form = RegistrationForm(instance=registration)
    except Registration.DoesNotExist:
        # Handle invalid or expired registration ID
        # return redirect('invalid_registration')
        return HttpResponse('invalid_registration')

    return render(request, 'registration/content_update.html', {'form': form})

def success(request):
   
    return render(request, 'registration/success.html')

