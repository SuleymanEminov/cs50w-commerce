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
        

class CommentForm(forms.ModelForm):
    " Form for Comments "
    class Meta:
        model = Comment
        fields = ('body',)


