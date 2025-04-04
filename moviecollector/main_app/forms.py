from django import forms
from .models import Critic

class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ['source', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '100'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        source = self.cleaned_data.get('source')

       
        if source == 'I' and rating is not None:
                return round(rating, 1)
            
        elif source in ['RT', 'M'] and rating is not None:
                return round(rating)
            
        return rating
