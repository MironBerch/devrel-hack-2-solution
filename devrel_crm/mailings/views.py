from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View

from accounts.models import User
from config.settings import EMAIL_HOST_USER
from mailings.forms import EmailForm


class Mailings(View):
    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            emails = User.objects.values_list('email', flat=True)
            send_mail(subject, message, EMAIL_HOST_USER, emails)
        return render(request, 'mailings_page.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = EmailForm()
        return render(request, 'mailings_page.html', {'form': form})
