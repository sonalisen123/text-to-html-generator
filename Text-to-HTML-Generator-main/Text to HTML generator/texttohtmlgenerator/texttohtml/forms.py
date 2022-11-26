


from django import forms
from .models import Text
from ckeditor.widgets import CKEditorWidget

class TextForm(forms.ModelForm):
    textarea = forms.CharField(widget=CKEditorWidget() , label="Text Editor")
    class Meta:
        model=Text
        fields = ('textarea',)