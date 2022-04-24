from django import forms
from .models import *
  
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing 
        fields = ['title',
                'image',
                'description',
                'price',
                'category',
                ]
    def __init__(self, *args, **kwargs):
            super(ListingForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
        # widgets = {
        #     'title': forms.TextInput(label='',attrs={
        #         "class":"form-control mt-4",
        #         "id":"exampleFormControlTextarea1"}),
        #     'description': forms.Textarea(attrs={
        #         'cols': 80, 
        #         'rows': 7, 
        #         'class':"form-group",
        #         "id": "exampleFormControlTextarea1"}),
        # }


