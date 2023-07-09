from django import forms
from .models import OneDoc, TwoDoc, Main, Doc
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError


class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = ['main']


class DocForm(forms.ModelForm):
    # hand_text = forms.CharField(required=False)

    class Meta:
        model = Doc
        fields = '__all__'

    def clean(self):
        super().clean()
        if not any([self.cleaned_data['file'], self.cleaned_data['text']]):
            raise ValidationError(
                'File or Text must be added!'
            )


    # def save(self, commit=True):
    #     instance = super(DocForm, self).save(commit=False)
    #     instance.file = ContentFile(self.cleaned_data['text'], 'some_save.txt')
    #     if commit:
    #         instance.save()
    #     return instance
