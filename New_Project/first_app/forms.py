from django import forms
from django.core import validators
from .models import User_Info

#custom validation function
# def check_for_z(value):
#     if value[0].lower != 'z':
#         raise forms.ValidationError("NAME STARTS WITH Z")

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    # verify Email
    verify_email = forms.EmailField(label="Enter Your Email Again:")
    text = forms.CharField(widget = forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("MAKE SURE BOTH EMAILS ARE SAME")



    #hiddend field
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # this function is use to validate bot 
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT !")
    #     return botcatcher

# Model Base Form
class User_Modle_Form(forms.ModelForm):
    class Meta():
        model = User_Info
        fields = '__all__'