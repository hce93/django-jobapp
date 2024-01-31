from django import forms
from django.core.validators import validate_email
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

def validate_comma(value):
    if "," in value:
        raise forms.ValidationError("Invalid Entry")
    return value

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        
        # exclude fields you don't want to render
        # exclude=('first_name',)
        
        # customise labels displayed on the template
        labels = {
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email'),
        }
        # help_texts = {
        #     'first_name':_('Enter characters only')
        # }
        
        error_messages = {
            'first_name':{
                'required':_('You cannot move forward without the first name')
            }
        }

# class SubscribeForm(forms.Form):
    # first_name = forms.CharField(max_length=100, required=False, label="First Name", help_text="Enter First Name")
    # last_name = forms.CharField(max_length=100, validators=[validate_comma])
    # email = forms.EmailField(max_length=100)
    
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return data
