#!/usr/bin/env python
"""
Created on 4/12/18

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
from django import forms
from lists.models import Item

EMPTY_LIST_ERROR = 'You cannot have an empty list item'


# class ItemForm(forms.Form):
#     item_text = forms.CharField(
#         widget=forms.fields.TextInput(
#             attrs={
#                 'placeholder': 'Enter a to-do item',
#                 'class': 'form-control input-lg',
#             }
#         )
#     )

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(
                attrs={
                    'placeholder': 'Enter a to-do item',
                    'class': 'form-control input-lg',
                }
            )
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }
