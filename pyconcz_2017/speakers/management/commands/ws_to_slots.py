import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from pyconcz_2017.speakers.models import Slot, Workshop


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--ws-id', dest='ws_id', type=int, help='ws id')

    def handle(self, *args, **options):
        qs = Workshop.objects.all() if not options['ws_id'] else Workshop.objects.filter(id=options['ws_id'])

        for one in Workshop.objects.all():
            Slot.objects.create(
                date=timezone.make_aware(datetime.datetime(settings.WORKSHOPS_DATES[0].year,
                                                           settings.WORKSHOPS_DATES[0].month,
                                                           settings.WORKSHOPS_DATES[0].day,
                                                           ),
                                         timezone.get_current_timezone()),
                content_object=one,
                room=settings.WORKSHOPS_ROOMS[0][0],
            )

        self.stdout.write(self.style.SUCCESS('Copied %d wss' % qs.count()))
