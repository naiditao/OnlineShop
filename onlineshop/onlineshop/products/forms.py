from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1,max_value=5)
    text = forms.CharField(label = "Feedback", widget=forms.Textarea, max_length=300)