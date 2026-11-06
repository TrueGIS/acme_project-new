# birthday/forms.py
from django import forms
from django.core.exceptions import ValidationError

# Импортируем класс модели Birthday
from .models import Birthday


BEATLES = {
    'Джон Леннон',
    'Пол Маккартни',
    'Джордж Харрисон',
    'Ринго Старр',
}


# Для использования формы с моделями меняем класс на forms.ModelForm
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей

    # Все настройки задаём в подклассе Meta
    class Meta:
        # Указываем модель, на основе которой должна строиться форма
        model = Birthday
        # Явно перечисляем поля, доступные пользователю
        fields = ('first_name', 'last_name', 'birthday', 'image')
        widgets = {            
            'birthday': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
        }

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам 
        # и возвращаем только первое имя
        return first_name.split()[0]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if (
            first_name
            and last_name
            and f'{first_name} {last_name}' in BEATLES
        ):
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, '
                'настоящее имя!',
            )

        return cleaned_data
