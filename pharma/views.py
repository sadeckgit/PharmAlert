import datetime
import random

from django.shortcuts import render, get_object_or_404
from .models import Pharmacy, Advice
from accounts.models import UserProfile


# Create your views here.
def index(request):
    opened = 0
    opened_in_country = 0
    pharmacies = Pharmacy.objects.all()

    users = UserProfile.objects.all()

    for pharmacy in pharmacies:
        for profile in users:
            if profile.country == pharmacy.country:
                opened_in_country += 1
                if profile.town == pharmacy.town:
                    if pharmacy.status == 'OPEN':
                        opened += 1
                        print(opened, "pharmacy are opened in", pharmacy.town)

    date = datetime.datetime.now()
    print(date)

    advices = Advice.objects.all()
    total_advices = Advice.objects.count()
    advice_id = random.randint(1, total_advices)

    selected_advice = ""
    for advice in advices:
        if advice.id == advice_id:
            selected_advice = advice

    context = {'pharmacies': pharmacies,
               'users': users,
               'date': date,
               'opened': opened,
               'tip': selected_advice}

    return render(request, 'pharma/index.html', context)


def localisation(request, slug):
    details = get_object_or_404(Pharmacy, slug=slug)
    return render(request, 'pharma/localisation.html', context={'localisation': details})
