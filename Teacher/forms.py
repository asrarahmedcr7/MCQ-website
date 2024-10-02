from django import forms
from Student.models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class':'form-control border'
            }),
            'description' : forms.Textarea(attrs={
                'class':'form-control border'
            })
        }