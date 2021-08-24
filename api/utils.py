from datetime import (
    date,
    timedelta,
)
from .models import (
    Feast,
    ControlledBeverage,
)
from ext_data.models import (
    ABCPrice,
    format_abc_product_avg_column_name,
    format_abc_product_best_column_name,
)

from .constants import DEALS_MIN_PRICE_SCORE

def get_email_date_range():
    start_date = date.today() + timedelta(days=1)
    end_date = start_date + timedelta(days=7)
    return (start_date, end_date)

def get_email_feasts_products(start_date, end_date, latest_pull_date):
    feasts = Feast.objects.filter(date__range=(start_date, end_date))

    _feasts = []
    _products = []
    _unique_product_ids = []

    for feast in feasts:

        _feast = {
            'name': feast.name,
            'date': feast.date.strftime('%B %d'),
            'url': 'https://www.catholicculture.org/culture/liturgicalyear/calendar/day.cfm?date={}'.format( feast.date.strftime('%Y-%m-%d') ),
        }

        cocktails = feast.cocktails.all()

        _cocktails = []
        for cocktail in cocktails:

            _cocktail = {
                'name': cocktail.name,
                'instructions': cocktail.instructions,
            }

            _ingredients = []

            cocktail_ingredients = cocktail.ingredients.all()

            for cocktail_ingredient in cocktail_ingredients:

                ingredient = cocktail_ingredient.ingredient
                if ingredient.is_controlled:

                    products = ControlledBeverage.objects \
                                .filter(ingredients__in=[ingredient.pk])

                    _ingredient = {
                        'name': ingredient.name,
                        'is_controlled': True,
                        'amount': cocktail_ingredient.amount,
                        'measurement': cocktail_ingredient.measurement,
                    }
                    # print(ingredient, products)
                    for product in products:

                        # print(product.name)
                        if hasattr(product, 'abcproduct'):
                            abcproduct = product.abcproduct
                            _product = {
                                'id': abcproduct.id,
                                'name': abcproduct.name,
                            }

                            prices = ABCPrice.objects \
                                        .filter(product=abcproduct) \
                                        .filter(pull_date=latest_pull_date)
                            _prices = []

                            price_index = 0
                            for price in prices:

                                best_price_column_name = format_abc_product_best_column_name(price.size)
                                best_price = getattr(abcproduct, best_price_column_name)
                                amount_above_best_price = (price.current_price - best_price) if best_price else 0

                                avg_price_column_name = format_abc_product_avg_column_name(price.size)
                                avg_price_per_size = getattr(abcproduct, avg_price_column_name)

                                if avg_price_per_size:
                                    price_below_average_per_size = avg_price_per_size - price.current_price
                                else:
                                    price_below_average_per_size = 'N/A'

                                _prices.append({
                                    'current_price': price.current_price,
                                    'size': price.size,
                                    'price_below_average_per_liter': (abcproduct.avg_price_per_liter - price.price_per_liter),
                                    'price_below_average_per_size': price_below_average_per_size,
                                    'price_score': price.price_score,
                                    'price_per_liter_score': price.price_per_liter_score,
                                    'is_on_sale': price.is_on_sale,
                                    'url': '{}?productSize={}'.format(abcproduct.url, price_index), # TODO store the actual URL
                                    'amount_above_best_price': amount_above_best_price,
                                    'price_per_liter': price.price_per_liter,
                                })
                                price_index = price_index+1
                                _prices.sort(key=lambda item: item['price_score'], reverse=True)

                            _product['prices'] = _prices

                            # prevent duplicates
                            if _product['id'] not in _unique_product_ids:
                                _products.append(_product)
                                _unique_product_ids.append(_product['id'])

                    _ingredients.append(_ingredient)
                else:
                    _ingredients.append({
                        'name': ingredient.name,
                        'is_controlled': False,
                        'amount': cocktail_ingredient.amount,
                        'measurement': cocktail_ingredient.measurement,
                    })

            _cocktail['ingredients'] = _ingredients
            _cocktails.append(_cocktail)

        _feast['cocktails'] = _cocktails
        _feasts.append(_feast)
    return ( _feasts, _products )

def get_email_deals(latest_pull_date):

    # duplicate logic between here and send_abc_deals, find one place for it to live
    limit = None
    deals = []

    prices = ABCPrice.objects.filter(pull_date=latest_pull_date)
    for price in prices:
        if price.price_score > 70:

            if not limit or price.current_price <= limit:

                avg_price = price.avg_price
                best_price = price.best_price


                avg_price_column_name = format_abc_product_avg_column_name(price.size)
                avg_price_per_size = getattr(price.product, avg_price_column_name)
                price_below_average_per_size = avg_price_per_size - price.current_price

                deals.append({
                    'name': price.product.name,
                    'size': price.size,
                    'current_price': price.current_price,
                    'is_on_sale': price.is_on_sale,
                    'price_below_average': (avg_price - price.current_price),
                    'price_below_average_per_size': price_below_average_per_size,
                    'score': price.price_score,
                    'is_best_price': best_price==price.current_price,
                    'product_size': price.product_size,
                    'url': price.product.url,
                })

    deals = sorted(deals, key = lambda i: i['price_below_average'], reverse=True)

    return deals