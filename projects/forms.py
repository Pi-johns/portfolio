from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full p-3 text-gray-200 bg-gray-800 border border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500',
            'rows': 3,
            'placeholder': 'Cast your magical comment here... ✨'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']
