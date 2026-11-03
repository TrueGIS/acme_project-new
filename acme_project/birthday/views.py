from django.shortcuts import render

from .forms import BirthdayForm


def birthday(request):
    form = BirthdayForm(request.GET or None)
    if form.is_valid():
        birthday = form.cleaned_data["birthday"]
    else:
        return render(request, 'birthday/birthday.html', {'form': form})
