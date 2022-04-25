from django.forms import ModelForm
from home_app.models import Thestart

class thestartform(ModelForm):
    class Meta:
        model = Thestart
        fields = ['expense', 'price']