# coding: utf-8

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from email_confirm_la.models import EmailConfirmation
from email_confirm_la.exceptions import EmailConfirmationExpired

def confirm_email(request, confirmation_key):
    try:
        email_confirmation = EmailConfirmation.objects.get(confirmation_key=confirmation_key)
        email_confirmation.confirm()
    except (EmailConfirmation.DoesNotExist, EmailConfirmationExpired):
        return render(request, 'email_confirm_la/email_confirm_fail.html')

    context = {
        'email_confirmation': email_confirmation,
        'email_confirm': True,
    }

    return HttpResponseRedirect(reverse('confirm'))
