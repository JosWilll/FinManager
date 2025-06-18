from django import forms
from .models import *

from django.forms import NumberInput
# Ми можемо створювати форми, просто створивши їхній клас,
# а потім додавши туди Meta-клас зі вказанням моделі та 
# переліком полів, задіяних у формі


# Форма транзакцій
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "account",
            "tsum",
            "isExpense",
            "category",
            "comment",
            "checkID",
            "tDateTime",
        ]

        widgets = {
            "tDateTime": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        }
    
    tsum = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter amount"})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
    )

    comment = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "Optional comment"}),
        required=False
    )

    checkID = forms.ModelChoiceField(
        queryset=Check.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,  # Робимо поле необов'язковим
        blank=True
    )

    def __init__(self, *args, is_expense=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        if is_expense is not None:
            # Фільтруємо категорії в залежності від is_expense
            self.fields["category"].queryset = Category.objects.filter(isExpense=(is_expense == "expense"))

            # Якщо вибрана категорія, встановлюємо isExpense
            if self.instance.pk:  # Якщо обробляємо існуючий об'єкт
                selected_category = self.instance.category
                self.initial["isExpense"] = selected_category.isExpense
            elif is_expense == "expense":
                self.initial["isExpense"] = True
            else:
                self.initial["isExpense"] = False

    def clean_isExpense(self):
        return self.initial.get("isExpense")


    
# Форма категорій
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "title",
            "isExpense",
        ]
