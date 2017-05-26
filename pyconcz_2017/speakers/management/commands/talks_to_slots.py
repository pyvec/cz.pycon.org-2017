import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from pyconcz_2017.speakers.models import Slot, Talk


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--talk-id', dest='talk_id', type=int, help='talk id')

    def handle(self, *args, **options):
        qs = Talk.objects.all() if not options['talk_id'] else Talk.objects.filter(id=options['talk_id'])

        for one in qs:
            Slot.objects.create(
                date=timezone.make_aware(datetime.datetime(settings.TALKS_DATES[0].year,
                                                           settings.TALKS_DATES[0].month,
                                                           settings.TALKS_DATES[0].day,
                                                           ),
                                         timezone.get_current_timezone()),
                content_object=one,
                room=settings.TALKS_ROOMS[0][0],
            )
