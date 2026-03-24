from django import forms
from django.forms import ModelForm, Textarea, FileInput
from django.core.exceptions import ValidationError

from .models import Application

# =============== Application Form ===============
class ApplicationForm(ModelForm):

    class Meta:
        model = Application
        fields = ['resume', 'cover_letter']
        widgets = {
            'resume': FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
            }),
            'cover_letter': Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Optional: Write a cover letter',
            }),
        }
        labels = {
            'resume': 'Upload Resume',
            'cover_letter': 'Cover Letter (Optional)',
        }

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if resume.size > 2 * 1024 * 1024: 
                raise ValidationError("Resume file too large (max 2MB).")
            if not resume.name.endswith(('.pdf', '.doc', '.docx')):
                raise ValidationError("Resume must be a PDF or Word document.")
        return resume
    
    def clean_cover_letter(self):
        cover_letter = self.cleaned_data.get('cover_letter', '')
        if cover_letter and len(cover_letter) > 2000:
            raise ValidationError("Cover letter cannot exceed 2000 characters.")
        return cover_letter