from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version, Category

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


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views", "created_at", "updated_at", "owner")

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


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("category", "description", "is_published")


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"


class CategoryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

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



