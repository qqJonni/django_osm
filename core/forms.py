from django import forms
from django.forms import Textarea
from core.models import PlaceName, PlaceImage, Comment


class PlaceImageForm(forms.ModelForm):
    picture = forms.FileField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = PlaceImage
        fields = ['picture']


class PlaceForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите название места'}))
    short_description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите короткое описание места'}))
    long_description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите основное описание места'}))
    latitude = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите координаты широты'}))
    longitude = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите координаты долготы'}))

    class Meta:
        model = PlaceName
        fields = ['title', 'short_description', 'long_description', 'category', 'latitude', 'longitude']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows': 5})
