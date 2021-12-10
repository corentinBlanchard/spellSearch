from django.contrib.auth import login, authenticate
from django import forms
from .models import Classes

class SearchForm(forms.Form):
    choices = []
    for c in Classes.objects.all():
        choices.append((c.id,c.name))

    name = forms.CharField(max_length=200)
    is_verbal = forms.BooleanField()
    is_somatic = forms.BooleanField()
    is_material = forms.BooleanField()
    max_level = forms.IntegerField(initial=10)
    classes = forms.MultipleChoiceField(choices=choices)

    class Meta:
        fields = ["name", "is_verbal", "is_somatic", "is_material", "max_level", "classes"]
    

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['is_verbal'].required = False
        self.fields['is_somatic'].required = False
        self.fields['is_material'].required = False
        self.fields["max_level"].required = False
        self.fields["classes"].required = False

