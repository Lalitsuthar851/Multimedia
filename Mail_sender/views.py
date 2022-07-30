from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def email_home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        msg = request.POST.get("message")

        recipient_list = [email,
                          ]
        send_mail(subject,
                   msg,
                   settings.EMAIL_HOST_USER,
                   recipient_list
                   )
        return redirect("email_home")

    return render(request,
              "Write_email.html",
              {"name": settings.EMAIL_HOST_USER})
