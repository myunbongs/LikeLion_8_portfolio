from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    title = forms.CharField(
        label="제목:",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autofocus':'True',
            'placeholder': "제목을 입력해 주세요",
            'style':'margin: 10px auto; width:50%;',
        })
    )
    content = forms.CharField(
        label="내용:",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "내용을 입력해 주세요",
            'style':'margin: 10px auto; width:50%;',
            'cols': 50, 'rows': 13
        })
    )


    class Meta:
        model = Portfolio
        fields = ['portfolio', 'title', 'content']