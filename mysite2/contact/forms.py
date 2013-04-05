#-*-coding:UTF-8-*-
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    email   = forms.EmailField(required=False,label='Your e-mail')
    message = forms.CharField(widget = forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message.split())<4:
            raise forms.ValidationError('请输入至少四字。')
        return message