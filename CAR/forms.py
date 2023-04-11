from django import forms

from . import models


class ReviewsCreateForm(forms.ModelForm):
    class Meta:
        model = models.ReviewsCar
        fields = "__all__"


class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarShop
        fields = "__all__"
