from django import forms
from .models import Recipe

CATEGORY_SUBCATEGORY_MAP = {
    'daily': ['breakfast', 'lunch', 'dinner', 'dessert', 'drinks'],
    'holiday': ['new_years', 'mothers_day'],
    'health': ['keto', 'vegetarian'],
}


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'ingredients',
            'instructions',
            'image',
            'main_category',
            'sub_category'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Short description'
            }),
            'ingredients': forms.HiddenInput(),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Cooking instructions'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'main_category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'sub_category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        main_category = cleaned_data.get('main_category')
        sub_category = cleaned_data.get('sub_category')
        ingredients = cleaned_data.get('ingredients')
        image = cleaned_data.get('image')

        if main_category and sub_category:
            allowed_subcategories = CATEGORY_SUBCATEGORY_MAP.get(main_category, [])
            if sub_category not in allowed_subcategories:
                self.add_error(
                    'sub_category',
                    f"'{sub_category}' is not valid for '{main_category}'."
                )

        if not ingredients or not ingredients.strip():
            self.add_error(
                'ingredients',
                "Please add at least one ingredient."
            )

        if not image:
            self.add_error(
                'image',
                "Please upload an image."
            )

        return cleaned_data