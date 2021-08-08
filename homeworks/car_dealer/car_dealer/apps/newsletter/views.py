from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from apps.newsletter.forms import SubscriberForm
from django.urls import reverse
from apps.newsletter.models import Subscribers



class NewsLetterModelForm(FormView):
    form_class = SubscriberForm
    template_name = 'newsletter/subscribe.html'
    success_url = '/subscribe/succes'

    def form_valid(self, form):
        subscriber = form.cleaned_data['email']
        try:
            return redirect('/subscribe/'+Subscribers.objects.get(email=subscriber).email)
        except(Subscribers.DoesNotExist,):
            Subscribers.objects.create(email=subscriber)
        return super().form_valid(form)



def succes_new_subscriber(request):
    return render(
        request,
        'newsletter/succes.html',
    )


def already_subscribe(request, email):
    return render(
        request,
        'newsletter/already_sub.html',
        {'email': email}
    )