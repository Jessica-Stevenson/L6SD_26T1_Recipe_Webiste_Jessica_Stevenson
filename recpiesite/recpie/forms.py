from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):

    ingredients = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe title'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Cooking instructions'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }