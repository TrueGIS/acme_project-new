# birthday/views.py
from django.shortcuts import render

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


def birthday(request):
    form_data = request.POST if request.method == "POST" else None
    form = BirthdayForm(form_data)
    context = {"form": form}

    if form.is_valid():
        saved_birthday = form.save()
        context.update(
            {
                "birthday_countdown": calculate_birthday_countdown(
                    saved_birthday.birthday,
                ),
                "first_name": saved_birthday.first_name,
                "last_name": saved_birthday.last_name,
                "show_result": True,
            }
        )

    return render(request, "birthday/birthday.html", context)


def birthday_list(request):
    # Получаем все объекты модели Birthday из БД
    birthdays = Birthday.objects.all().order_by("first_name")
    # Передаём их в контекст шаблона
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)
