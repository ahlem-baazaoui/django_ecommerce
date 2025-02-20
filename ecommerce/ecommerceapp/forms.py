from django import forms
from .models import Member

class MemberForm(forms.ModelForm):

   class Meta:
      model = Member
      fields = ["full_name", "email","twitter", "linkedin", "facebook", "website", "picture"]

picture = forms.FileField(required=False)  # <- Rendre le champ optionnel

