from django.core import management
from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
from django.db.models import Max
from api.models import (
    Feast,
    ControlledBeverage,
)
from ext_data.models import (
    ABCPrice,
    format_abc_product_best_column_name,
    get_latest_price_pull_date,
)
# from util.util import Email
from datetime import (
    date,
    timedelta,
    datetime,
)

from django.template.loader import render_to_string
from django.core.mail import send_mail

from api.utils import (
    get_email_date_range,
    get_email_feasts_products,
    get_email_deals,
)

from api.constants import (
    PRICE_PER_SIZE_SCORE_PERCENT,
    PRICE_PER_LITER_SCORE_PERCENT,
    DEALS_MIN_PRICE_SCORE,
)


class Command(BaseCommand):
    help = 'Sends an e-mail with Drinking with the Saints Cocktail Recomendations'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        # update the year of all past feast dates
        management.call_command('update_feast_year')

        (start_date, end_date) = get_email_date_range()
        latest_pull_date = get_latest_price_pull_date()

        ( feasts, products ) = get_email_feasts_products(start_date, end_date, latest_pull_date)
        deals = get_email_deals(latest_pull_date)

        message = render_to_string('api/templates/email.txt', {
            'feasts': feasts,
            'products': products,
            'start_date': start_date.strftime('%B %d'),
            'end_date': end_date.strftime('%B %d'),
            'latest_pull_date': latest_pull_date.strftime('%B %d, %Y'),
            'price_per_liter_score_percent': str(int(PRICE_PER_LITER_SCORE_PERCENT * 100)),
            'price_per_size_score_percent': str(int(PRICE_PER_SIZE_SCORE_PERCENT * 100)),
            'deals_min_price_score': DEALS_MIN_PRICE_SCORE,
        })

        html_message = render_to_string('api/templates/email.html', {
            'feasts': feasts,
            'products': products,
            'deals': deals,
            'start_date': start_date.strftime('%B %d'),
            'end_date': end_date.strftime('%B %d'),
            'latest_pull_date': latest_pull_date.strftime('%B %d, %Y'),
            'price_per_liter_score_percent': str(int(PRICE_PER_LITER_SCORE_PERCENT * 100)),
            'price_per_size_score_percent': str(int(PRICE_PER_SIZE_SCORE_PERCENT * 100)),
            'deals_min_price_score': DEALS_MIN_PRICE_SCORE,
        })

        recipient_list = settings.EMAIL_RECIPIENTS

        success = send_mail(
            subject='Bevendo: Your Weekly Drinking with the Saints Cocktails',
            from_email=settings.SENDER_EMAIL,
            recipient_list=recipient_list,
            message=message,
            html_message=html_message,
        )
        # print(success)
        # print(html_message)
        # print(message)

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('send_cocktail_recommendations script ran', dt_string)