# birthday/views.py
from django.shortcuts import render

from .forms import BirthdayForm
from .utils import calculate_birthday_countdown


def birthday(request):
    form = BirthdayForm(request.GET or None)
    context = {"form": form}

    if form.is_valid():
        cleaned_data = form.cleaned_data
        context.update(
            {
                "birthday_countdown": calculate_birthday_countdown(
                    cleaned_data["birthday"],
                ),
                "first_name": cleaned_data["first_name"],
                "last_name": cleaned_data["last_name"],
                "show_result": True,
            }
        )

    return render(request, "birthday/birthday.html", context)
