from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=64,
        widget=forms.TextInput({"class": "input-field input-default"}),
        label="Título",
    )
    description = forms.CharField(
        widget=forms.Textarea({"class": "input-field input-default resize-none"}),
        required=False,
        label="Descrição",
    )
    priority = forms.IntegerField()
    finish_date = forms.DateField(
        widget=forms.DateInput({"class": "input-field input-default", "type": "date"}, "%Y-%m-%d"),
        required=False,
        label="Data de finalização",
    )
