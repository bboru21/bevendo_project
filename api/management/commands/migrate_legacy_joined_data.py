from django.core.management.base import BaseCommand, CommandError
from django.db import connections, transaction
from api.models import (
    Ingredient,
    ControlledBeverage,
    CocktailIngredient,
    Cocktail,
    Feast,
)

class Command(BaseCommand):

    help = '''
        Script for migrating old bevendo joined database tables into api app:

            api_controlledbeverage_ingredients
            api_feast_cocktails
            api_cocktail_ingredients
    '''

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        '''
            Tables to copy data from:
                api_controlledbeverage_ingredients
                api_feast_cocktails
                api_cocktail_ingredients
        '''
        with connections['legacy'].cursor() as legacy_cursor:
            with connections['default'].cursor() as cursor:

                legacy_cursor.execute('''
                    PRAGMA table_info(api_feast_cocktails)
                ''')
                print(legacy_cursor.fetchall())

                cursor.execute('''
                    PRAGMA table_info(api_feast_cocktails)
                ''')
                print(cursor.fetchall())

                legacy_cursor.execute('''
                    SELECT id, feast_id, cocktail_id
                    FROM api_feast_cocktails
                ''')

                with transaction.atomic():
                    for ( id, feast_id, cocktail_id ) in legacy_cursor.fetchall():
                        print(id, feast_id, cocktail_id)
                        cursor.execute(f'''
                            INSERT INTO api_feast_cocktails (id, feast_id, cocktail_id)
                            VALUES ({id}, {feast_id}, {cocktail_id})
                        ''')

                cursor.execute('''
                    SELECT count(id)
                    FROM api_feast_cocktails
                ''')
                print(cursor.fetchone())

        with connections['legacy'].cursor() as legacy_cursor:
            with connections['default'].cursor() as cursor:

                legacy_cursor.execute('''
                    PRAGMA table_info(api_controlledbeverage_ingredients)
                ''')
                print(legacy_cursor.fetchall())

                cursor.execute('''
                    PRAGMA table_info(api_controlledbeverage_ingredients)
                ''')
                print(cursor.fetchall())

                legacy_cursor.execute('''
                    SELECT id, controlledbeverage_id, ingredient_id
                    FROM api_controlledbeverage_ingredients
                ''')

                with transaction.atomic():
                    for ( id, controlledbeverage_id, ingredient_id ) in legacy_cursor.fetchall():
                        print(id, controlledbeverage_id, ingredient_id)
                        cursor.execute(f'''
                            INSERT INTO api_controlledbeverage_ingredients (id, controlledbeverage_id, ingredient_id)
                            VALUES ({id}, {controlledbeverage_id}, {ingredient_id})
                        ''')

                cursor.execute('''
                    SELECT count(id)
                    FROM api_controlledbeverage_ingredients
                ''')
                print(cursor.fetchone())

        with connections['legacy'].cursor() as legacy_cursor:
            with connections['default'].cursor() as cursor:

                legacy_cursor.execute('''
                    PRAGMA table_info(api_cocktail_ingredients)
                ''')
                print(legacy_cursor.fetchall())

                cursor.execute('''
                    PRAGMA table_info(api_cocktail_ingredients)
                ''')
                print(cursor.fetchall())

                legacy_cursor.execute('''
                    SELECT id, cocktail_id, cocktailingredient_id
                    FROM api_cocktail_ingredients
                ''')

                with transaction.atomic():
                    for ( id, cocktail_id, cocktailingredient_id ) in legacy_cursor.fetchall():
                        print(id, cocktail_id, cocktailingredient_id)
                        cursor.execute(f'''
                            INSERT INTO api_cocktail_ingredients (id, cocktail_id, cocktailingredient_id)
                            VALUES ({id}, {cocktail_id}, {cocktailingredient_id})
                        ''')

                cursor.execute('''
                    SELECT count(id)
                    FROM api_cocktail_ingredients
                ''')
                print(cursor.fetchone())




