from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from .models import get_duration
from .models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    this_passcard_visits = []

    current_passcard = Passcard.objects.get(passcode=passcode)

    visits = Visit.objects.filter(passcard=current_passcard)

    for visit in visits:
        duration = get_duration(visit)
        is_strange = is_visit_long(duration)

        this_passcard_visits.append({
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': duration,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
