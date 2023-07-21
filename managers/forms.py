from django import forms

from .models import Category, Size, Product


class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            "name":forms.widgets.TextInput(attrs={"placeholder":"Category Name"})
        }


class Sizeform(forms.ModelForm):
    class Meta:
        model = Size 
        fields = ["size"]

        widgets = {
            "size":forms.widgets.TextInput(attrs={"placeholder":"Size "})
        }


class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","category", "sizes", "price", "description", "image"]

        widgets = {
            "name":forms.widgets.TextInput(attrs={"placeholder":"Product Name", "class":"outline-none"}),
            "category":forms.widgets.TextInput(attrs={}),
            "sizes":forms.widgets.TextInput(attrs={}),
            "price":forms.widgets.NumberInput(attrs={"placeholder":"Product price"}),
            "description":forms.widgets.Textarea(attrs={"placeholder":"Product description"}),
            "image":forms.widgets.FileInput(attrs={}),



        }