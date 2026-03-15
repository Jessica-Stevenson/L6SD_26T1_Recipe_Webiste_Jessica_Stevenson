from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):

    ingredients = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Short description of the recipe'
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