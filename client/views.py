from django.shortcuts import render
from django.http import HttpResponse

from api.utils import get_email_deals
from ext_data.models import get_latest_price_pull_date

def index(request):

    latest_pull_date = get_latest_price_pull_date()
    deals = get_email_deals(latest_pull_date)

    context = {
        'deals': deals,
        'latest_pull_date': latest_pull_date.strftime('%B %d, %Y'),
    }

    return render(request, 'client/index.html', context)
