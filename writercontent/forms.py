from django import forms
from .models import Article
from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Article
        fields = ['title', 'content', 'status', 'tags']
