from django.shortcuts import render, redirect
from django.urls import reverse
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm

# Create your views here.

def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.POST:
        # Create a form instance with the data passed. This is binding data to the form
        subscribe_form = SubscribeForm(request.POST)
        # check if the form is valid
        print(subscribe_form)
        if subscribe_form.is_valid():
            print(subscribe_form)
            subscribe_form.save()
            # # get form data
            # email = subscribe_form.cleaned_data['email']
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            
            # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscribe.save()
            
            # redirect to thank you page
            return redirect(reverse('thank_you'))
            
    context = {"form":subscribe_form}
    return render(request, 'subscribe/subscribe.html', context)

def thank_you(request):
    return render(request, 'subscribe/thank_you.html')