from django import forms
from photo.models import *

class UploadPhotoForm(forms.Form):
    image_title = forms.CharField(label="Title")
    image = forms.ImageField(label= "Image")