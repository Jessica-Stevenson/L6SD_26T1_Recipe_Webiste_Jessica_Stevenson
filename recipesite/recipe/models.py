from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Recipe(models.Model):
    MAIN_CATEGORIES = [
        ('daily', 'Daily Recipes'),
        ('holiday', 'Holidays'),
        ('health', 'Diet & Health'),
    ]

    SUB_CATEGORIES = [
        # Daily
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('drinks', 'Drinks'),

        #Holidays
        ('new_years', "New Year's"),
        ('mothers_day', "Mother's Day"),

        #Health & Diet
        ('keto', 'Keto'),
        ('vegetarian', 'Vegetarian'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    # New fields
    main_category = models.CharField(max_length=20, choices=MAIN_CATEGORIES)
    sub_category = models.CharField(max_length=20, choices=SUB_CATEGORIES, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.sub_category:
            if self.main_category == 'daily' and self.sub_category not in ['breakfast', 'lunch', 'dinner', 'dessert', 'drinks']:
                raise ValidationError("Invalid subcategory for Daily Recipes.")

            if self.main_category == 'holiday' and self.sub_category not in ['new_years', 'mothers_day']:
                raise ValidationError("Invalid subcategory for Holidays.")

            if self.main_category == 'health' and self.sub_category not in ['keto', 'vegetarian']:
                raise ValidationError("Invalid subcategory for Health & Diet.")