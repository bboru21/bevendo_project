from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from django_nextjs.render import render_nextjs_page_sync

from api.models import CocktailIngredient
from api.utils import get_email_deals
from ext_data.models import get_latest_price_pull_date


def index(request):
    return render_nextjs_page_sync(request, 'client/index.html')

# def index(request):

#     latest_pull_date = get_latest_price_pull_date()
#     deals = get_email_deals(latest_pull_date)

#     cocktail_ingredients = CocktailIngredient.objects \
#         .filter(ingredient__is_controlled=True) \
#         .values('ingredient__name') \
#         .annotate(ingredient_count=Count('ingredient')) \
#         .order_by('-ingredient_count')

#     context = {
#         'cocktail_ingredients': cocktail_ingredients,
#         'deals': deals,
#         'latest_pull_date': latest_pull_date.strftime('%B %d, %Y'),
#     }

#     return render(request, 'client/index.html', context)
