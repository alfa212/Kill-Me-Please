from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from .models import get_duration


def format_duration(duration):
    output_duration = str(duration)[:-7]
    return output_duration


def storage_information_view(request):
    visitors_inside = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visit in visitors_inside:
        duration = get_duration(visit)
        duration_format = format_duration(duration)

        non_closed_visits.append({
            "who_entered": visit.passcard.owner_name,
            "entered_at": timezone.localtime(visit.entered_at),
            "duration": duration_format
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
