from django import forms 
from.models import Send_message,Denote_informations

class Denote_information_Form(forms.ModelForm):
    class Meta:
        model = Denote_informations
        fields = "__all__"
    fname=forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'boxs', 'placeholder':"First Name"}))
    lname=forms.CharField(label='',widget=forms.TextInput(
        attrs={'class': 'boxs', 'placeholder':"Last Name"}))
    email=forms.EmailField(label='',widget=forms.EmailInput(
        attrs={'class': 'boxs', 'placeholder':"E-mail"}
    ))
    phone=forms.CharField(label='',widget=forms.TextInput(
        attrs={'class': 'boxs', 'placeholder':"Phone Number"}))
        
    age=forms.IntegerField(label='',widget=forms.NumberInput(
        attrs={'class': 'boxs', 'placeholder':"Age"}
    ))
    
    class_room=forms.CharField(label='',widget=forms.TextInput(
        attrs={'class': 'boxs', 'placeholder':"Classroom"}))
    country=forms.CharField(label='',widget=forms.TextInput(
         attrs={'class': 'boxs', 'placeholder':"Country"}
    ))
    booktype=forms.CharField(label='',widget=forms.TextInput(
         attrs={'class': 'boxs', 'placeholder':"Book type"}
    ))
    message=forms.CharField(label='',widget=forms.TextInput(
        attrs={'placeholder':"Why register with us?"}
        ))
    #img=forms.ImageField(label='',widget=forms.ImageField(   ))
    img = forms.ImageField(label='')
# {{sform.as_p}}
class send_message_Form(forms.ModelForm):
    class Meta:
        model=Send_message
        fields = ['name','email','message']
    name=forms.CharField(label='Name:',widget=forms.TextInput(
         attrs={ 'placeholder':"Write your name here.."}
    ))
    email = forms.EmailField(label='Email: ',widget=forms.EmailInput(
         attrs={ 'placeholder':"Let us know how to contact you back.."}
    ))
    message=forms.CharField(label='Message: ',widget=forms.TextInput(
         attrs={ 'placeholder':"What would you like to tell us.."}
    ))