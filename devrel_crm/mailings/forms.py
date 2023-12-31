from ckeditor.widgets import CKEditorWidget

from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=CKEditorWidget())
