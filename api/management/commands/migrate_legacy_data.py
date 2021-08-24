from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from api.models import (
    Ingredient,
    ControlledBeverage,
    CocktailIngredient,
    Cocktail,
    Feast,
)

from ext_data.models import (
    ABCProduct,
    ABCPrice,
)

class Command(BaseCommand):

    help = '''
        Script for migrating old bevendo database into new one.
    '''

    def add_arguments(self, parser):
        parser.add_argument('--ingredient', action='store_true', default=False)
        parser.add_argument('--controlledbeverage', action='store_true', default=False)
        parser.add_argument('--cocktailingredient', action='store_true', default=False)
        parser.add_argument('--cocktail', action='store_true', default=False)
        parser.add_argument('--feast', action='store_true', default=False)
        parser.add_argument('--abcproduct', action='store_true', default=False)
        parser.add_argument('--abcprice', action='store_true', default=False)

    def handle(self, *args, **options):

        if options['ingredient']:
            with connections['legacy'].cursor() as cursor:

                cursor.execute('''
                    PRAGMA table_info(api_ingredient)
                ''')
                for row in cursor.fetchall():
                    print(row)
                '''
                (0, 'id', 'integer', 1, None, 1)
                (1, 'name', 'varchar(250)', 1, None, 0)
                (2, 'is_controlled', 'bool', 1, None, 0)
                '''

                cursor.execute('''
                    SELECT *
                    FROM api_ingredient
                ''')

                for row in cursor.fetchall():
                    obj = Ingredient.objects.create(
                        id=row[0],
                        name=row[1],
                        is_controlled=row[2],
                    )
                    print(obj)

                ingredients = Ingredient.objects.all()
                print(ingredients.count())

        if options['controlledbeverage']:

            with connections['legacy'].cursor() as cursor:

                cursor.execute('''
                    PRAGMA table_info(api_controlledbeverage)
                ''')
                for row in cursor.fetchall():
                    print(row)
                '''
                (0, 'id', 'integer', 1, None, 1)
                (1, 'name', 'varchar(250)', 1, None, 0)
                (2, 'is_in_stock', 'bool', 0, None, 0)
                '''
                ControlledBeverage.objects.all().delete()
                cursor.execute('''
                    SELECT *
                    FROM api_controlledbeverage
                ''')
                for row in cursor.fetchall():
                    # print(row)
                    obj = ControlledBeverage.objects.create(
                        id=row[0],
                        name=row[1],
                        is_in_stock=row[2],
                    )

                controlled_beverages = ControlledBeverage.objects.all()
                print(controlled_beverages.count())

        if options['cocktailingredient']:

            with connections['legacy'].cursor() as cursor:

                cursor.execute('''
                    PRAGMA table_info(api_cocktailingredient)
                ''')
                for row in cursor.fetchall():
                    print(row)
                '''
                (0, 'id', 'integer', 1, None, 1)
                (1, 'amount', 'decimal', 0, None, 0)
                (2, 'measurement', 'varchar(20)', 0, None, 0)
                (3, 'ingredient_id', 'integer', 1, None, 0)
                '''
                CocktailIngredient.objects.all().delete()
                cursor.execute('''
                    SELECT *
                    FROM api_cocktailingredient
                ''')
                for row in cursor.fetchall():
                    print(row)
                    obj = CocktailIngredient.objects.create(
                        id=row[0],
                        amount=row[1],
                        measurement=row[2],
                        ingredient_id=row[3],
                    )

                results = CocktailIngredient.objects.all()
                print(results.count())

        if options['cocktail']:

            with connections['legacy'].cursor() as cursor:

                cursor.execute('''
                    PRAGMA table_info(api_cocktail)
                ''')
                for row in cursor.fetchall():
                    print(row)
                '''
                (0, 'id', 'integer', 1, None, 1)
                (1, 'name', 'varchar(250)', 1, None, 0)
                (2, 'instructions', 'text', 0, None, 0)
                '''
                Cocktail.objects.all().delete()
                cursor.execute('''
                    SELECT *
                    FROM api_cocktail
                ''')
                for row in cursor.fetchall():
                    print(row)
                    obj = Cocktail.objects.create(
                        id=row[0],
                        name=row[1],
                        instructions=row[2],
                    )

                results = Cocktail.objects.all()
                print(results.count())

        if options['feast']:

            with connections['legacy'].cursor() as cursor:

                cursor.execute('''
                    PRAGMA table_info(api_feast)
                ''')
                for row in cursor.fetchall():
                    print(row)
                '''
                (0, 'id', 'integer', 1, None, 1)
                (1, 'date', 'date', 1, None, 0)
                (2, 'name', 'varchar(250)', 1, None, 0)
                '''
                Feast.objects.all().delete()
                cursor.execute('''
                    SELECT *
                    FROM api_feast
                ''')
                for row in cursor.fetchall():
                    print(row)
                    obj = Feast.objects.create(
                        id=row[0],
                        date=row[1],
                        name=row[2],
                    )

                results = Feast.objects.all()
                print(results.count())

        if options['abcproduct']:

            with connections['legacy'].cursor() as cursor:

                cursor.execute('''
                    PRAGMA table_info(ext_data_abcproduct)
                ''')
                for row in cursor.fetchall():
                    print(row)
                '''
                (0, 'id', 'integer', 1, None, 1)
                (1, 'name', 'varchar(250)', 0, None, 0)
                (2, 'url', 'varchar(1855)', 1, None, 0)
                (3, 'avg_price_per_liter', 'decimal', 0, None, 0)
                (4, 'best_price_per_liter', 'decimal', 0, None, 0)
                (5, 'best_price_50_ml', 'decimal', 0, None, 0)
                (6, 'best_price_100_ml', 'decimal', 0, None, 0)
                (7, 'best_price_200_ml', 'decimal', 0, None, 0)
                (8, 'best_price_375_ml', 'decimal', 0, None, 0)
                (9, 'best_price_473_18_ml', 'decimal', 0, None, 0)
                (10, 'best_price_750_ml', 'decimal', 0, None, 0)
                (11, 'best_price_1_l', 'decimal', 0, None, 0)
                (12, 'best_price_1_5_l', 'decimal', 0, None, 0)
                (13, 'best_price_1_75_l', 'decimal', 0, None, 0)
                (14, 'avg_price_50_ml', 'decimal', 0, None, 0)
                (15, 'avg_price_100_ml', 'decimal', 0, None, 0)
                (16, 'avg_price_200_ml', 'decimal', 0, None, 0)
                (17, 'avg_price_375_ml', 'decimal', 0, None, 0)
                (18, 'avg_price_473_18_ml', 'decimal', 0, None, 0)
                (19, 'avg_price_750_ml', 'decimal', 0, None, 0)
                (20, 'avg_price_1_l', 'decimal', 0, None, 0)
                (21, 'avg_price_1_5_l', 'decimal', 0, None, 0)
                (22, 'avg_price_1_75_l', 'decimal', 0, None, 0)
                (23, 'active', 'bool', 1, None, 0)
                (24, 'controlled_beverage_id', 'integer', 0, None, 0)
                '''

                cursor.execute('''
                    SELECT *
                    FROM ext_data_abcproduct
                ''')

                for row in cursor.fetchall():
                    obj = ABCProduct.objects.create(
                        id=row[0],
                        name=row[1],
                        url=row[2],
                        avg_price_per_liter=row[3],
                        best_price_per_liter=row[4],
                        best_price_50_ml=row[5],
                        best_price_750_ml=row[10],
                        best_price_1_l=row[11],
                        best_price_1_75_l=row[13],
                        controlled_beverage_id=row[24],
                        best_price_375_ml=row[8],
                        best_price_200_ml=row[7],
                        best_price_100_ml=row[6],
                        best_price_1_5_l=row[12],
                        best_price_473_18_ml=row[9],
                        avg_price_100_ml=row[15],
                        avg_price_1_5_l=row[21],
                        avg_price_1_75_l=row[22],
                        avg_price_1_l=row[20],
                        avg_price_200_ml=row[16],
                        avg_price_375_ml=row[17],
                        avg_price_473_18_ml=row[18],
                        avg_price_50_ml=row[14],
                        avg_price_750_ml=row[19],
                        active=row[23],
                    )
                    print(obj)

                print(ABCProduct.objects.count())

        if options['abcprice']:
            with connections['legacy'].cursor() as cursor:

                cursor.execute('''
                    PRAGMA table_info(ext_data_abcprice)
                ''')
                for row in cursor.fetchall():
                    print(row)
                '''
                (0, 'id', 'integer', 1, None, 1)
                (1, 'size', 'varchar(250)', 0, None, 0)
                (2, 'current_price', 'decimal', 1, None, 0)
                (3, 'price_per_liter', 'decimal', 1, None, 0)
                (4, 'discount_price', 'decimal', 0, None, 0)
                (5, 'retail_price', 'decimal', 0, None, 0)
                (6, 'is_on_sale', 'bool', 1, None, 0)
                (7, 'pull_date', 'datetime', 1, None, 0)
                (8, 'product_size', 'integer', 0, None, 0)
                (9, 'product_id', 'integer', 1, None, 0)
                '''

                cursor.execute('''
                    SELECT *
                    FROM ext_data_abcprice
                ''')

                for row in cursor.fetchall():
                    obj = ABCPrice.objects.create(
                        id=row[0],
                        size=row[1],
                        current_price=row[2],
                        price_per_liter=row[3],
                        discount_price=row[4],
                        retail_price=row[5],
                        is_on_sale=row[6],
                        pull_date=row[7],
                        product_id=row[9],
                        product_size=row[8],
                    )
                    print(obj)

                print(ABCPrice.objects.count())
