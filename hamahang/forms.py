from django import forms

from .models import mdl_Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=mdl_Contact
        fields=["first_name","last_name","mobile","subject"]

#    def __init__(self):
#        super(ContactForm, self).__init__()
        
#       self.first_name=forms.CharField(max_length=300) 
#        self.last_name=forms.CharField(max_length=300) 
#        self.subject=forms.TextField(max_length=4000)