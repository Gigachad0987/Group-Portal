from django import forms
from .models import Announcements
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ["name", "title", "content"]
    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})