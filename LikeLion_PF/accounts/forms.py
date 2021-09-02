from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(
        label="닉네임:",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autofocus':'True',
            'placeholder': "닉네임을 입력해 주세요",
            'style':'margin: 10px auto; width:50%;',
        })
    )
    description = forms.CharField(
        label="한줄 소개:",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "한줄 소개를 입력해 주세요",
            'style':'margin: 10px auto; width:50%;',
            'cols': 50, 'rows': 13
        })
    )
    image = forms.ImageField(
        label="프로필 사진 설정:",
        widget=forms.FileInput(attrs={
            "placeholder": ""
        })
    )

    class Meta:
        model = Profile
        fields = ['nickname', 'description', 'image']