from django.forms import ModelForm, forms, BooleanField

from blog.models import Blog, Version

forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ("views", "owner",)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Название не должно содержать запрещённых слов')
            else:
                return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError('Описание не должно содержать запрещённых слов')
        return cleaned_data

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"