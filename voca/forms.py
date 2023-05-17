from django import forms
from voca.models import Word,Example


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['subject', 'meaning']

        labels = {
            'subject': '단어',
            'meaning': '뜻',
        }

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ['content']
        labels = {
            'content': '예문',
        }