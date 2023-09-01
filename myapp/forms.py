from .models import MyModel
from django.forms import ModelForm
class ImageForm(ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__"
    