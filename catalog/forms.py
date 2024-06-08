from django.forms import ModelForm, forms

from catalog.models import Product, Version

FORBIDDEN_WORDS = [
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


def clean(cleaned_data):
    for word in FORBIDDEN_WORDS:
        if word in cleaned_data.lower():
            raise forms.ValidationError(f"Название не может содержать слово: {word}")
    return cleaned_data


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("views", "created_at", "updated_at",)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")
        clean(cleaned_data)

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")
        clean(cleaned_data)


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


