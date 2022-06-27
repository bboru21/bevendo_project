import json

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from django_nextjs.render import render_nextjs_page_sync

from api.models import CocktailIngredient
from api.serializers import CocktailIngredientSerializer
from api.utils import get_email_deals
from ext_data.models import get_latest_price_pull_date


def index(request):
    latest_pull_date = get_latest_price_pull_date()
    deals = get_email_deals(latest_pull_date)

    # ingredients = CocktailIngredient.objects \
    #     .filter(ingredient__is_controlled=True) \
    #     .values('ingredient__name') \
    #     .annotate(ingredient_count=Count('ingredient')) \
    #     .order_by('-ingredient_count')

    # serialized_ingredients = CocktailIngredientSerializer(data=ingredients, many=True)
    # serialized_ingredients.is_valid(raise_exception=False)

    context = {
        'page_data': {
            'deals': deals,
            'latest_pull_date': latest_pull_date,
        },
    }
    return render_nextjs_page_sync(request, 'client/index.html', context)
