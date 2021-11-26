from django.contrib.auth import login, authenticate
from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(max_length=200)
    is_verbal = forms.BooleanField()
    is_somatic = forms.BooleanField()
    is_material = forms.BooleanField()
    max_level = forms.IntegerField(initial=0)

    class Meta:
        fields = ["name", "is_verbal", "is_somatic", "is_material", "max_level"]
    

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['is_verbal'].required = False
        self.fields['is_somatic'].required = False
        self.fields['is_material'].required = False
        self.fields["max_level"].required = False

