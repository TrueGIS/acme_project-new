# birthday/views.py
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


def birthday(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None

    if request.method == "POST":
        form_data = request.POST
        form_files = request.FILES
    else:
        form_data = None
        form_files = None
    form = BirthdayForm(form_data, form_files, instance=instance)
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


def delete_birthday(request, pk):
    instance = get_object_or_404(Birthday, pk=pk)

    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')

    form = BirthdayForm(instance=instance)
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context)
