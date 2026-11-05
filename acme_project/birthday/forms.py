# birthday/forms.py
from django import forms

# Импортируем класс модели Birthday
from .models import Birthday


# Для использования формы с моделями меняем класс на forms.ModelForm
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей

    # Все настройки задаём в подклассе Meta
    class Meta:
        # Указываем модель, на основе которой должна строиться форма
        model = Birthday
        # Явно перечисляем поля, доступные пользователю
        fields = ('first_name', 'last_name', 'birthday')
        widgets = {            
            'birthday': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
        }
