from django import forms

class AnalyzeForm(forms.Form):
    position = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Job Position"
        })
    )

    company_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Company Name"
        })
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Paste Job Description Here...",
            "rows": 6
        })
    )

    resume_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control"
        })
    )