from .models import PostModel,sort
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = ('username','Email','year','states','image','gender','Remember_me','accept_Terms_Conditions','Description')
        widgets = {
            'Remember_me': forms.CheckboxInput,
            'accept_Terms_Conditions':forms.CheckboxInput,
            'gender':forms.RadioSelect
        }


class sortForm(forms.ModelForm):
    class Meta:
        model= sort
        fields=('sortchoices',)

