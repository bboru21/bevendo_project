import datetime

from django.core.management import BaseCommand
from django.db import transaction

from ext_data.models import (
    CalapiInadiutoriumLiturgicalDay,
    CalapiInadiutoriumCelebration,
)

from ext_data.calapi_inadiutorium_api import (
    CalapiInadiutoriumDateAPI,
)

class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument(
            '--pull',
            action='store_true',
            help='pull data from Calapi Inadiutorium API',
        )
        parser.add_argument(
            '--month',
            type=int,
            help='month for which to pull data',
        )
        parser.add_argument(
            '--year',
            type=int,
            help='year for which to pull data',
        )

        parser.add_argument(
            '--update',
            action='store_true',
        )

    def handle(self, **options):

        if options['pull']:
            api = CalapiInadiutoriumDateAPI()

            # data = api.get_liturgical_days_by_date_range()
            # print(data)

            # start_date = datetime.datetime.now() + datetime.timedelta(days=3)
            # end_date = start_date + datetime.timedelta(days=7)
            # data = api.get_liturgical_days_by_date_range(start_date, end_date)
            # print(data)

            # data = api.get_liturgical_days_by_month()
            # print(data)

            data = api.get_liturgical_days_by_year(2022)
            print(data)

            with transaction.atomic():
                for result in data['results']:

                    liturgical_day_obj, created = CalapiInadiutoriumLiturgicalDay.objects.update_or_create(
                        date = result['date'],
                        defaults = {
                            'season': result['season'],
                            'season_week': result['season_week'],
                            'weekday': result['weekday'],
                        }
                    )

                    print('liturgical_day', liturgical_day_obj.pk, created)

                    celebration_objs = []
                    for celebration in result['celebrations']:
                        celebration_obj, created = CalapiInadiutoriumCelebration.objects.update_or_create(
                            title = celebration['title'],
                            defaults = {
                                'colour': celebration['colour'],
                                'rank': celebration['rank'],
                                'rank_num': celebration['rank_num'],
                            },
                        )
                        celebration_objs.append(celebration_obj)

                        print('celebration', celebration_obj.pk, created)

                    liturgical_day_obj.celebrations.set( celebration_objs )



        if options['update']:

            start_date = datetime.date.fromisoformat('2021-11-27')
            end_date = datetime.date.fromisoformat('2021-12-26')

            days = CalapiInadiutoriumLiturgicalDay.objects.filter(date__range=(start_date, end_date))
            for day in days:
                print(day, day.season)
                for celebration in day.celebrations.all():
                    print('\t', celebration)

        print('finis')
