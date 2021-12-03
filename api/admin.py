from django.contrib import admin

from .models import (
    Cocktail,
    CocktailIngredient,
    Ingredient,
    Feast,
    ControlledBeverage,
)


class AutocompleteAdmin(admin.ModelAdmin):

    class Media:
        abstract = True
        # Hack to provide jQuery namespace for autocomplete-light libraries
        js = (
            'admin/js/vendor/jquery/jquery.min.js',
            'autocomplete_light/jquery.init.js',
        )


@admin.register(Cocktail)
class CocktailAdmin(AutocompleteAdmin):
    search_fields = (
        'name',
    )
    autocomplete_fields = (
        'ingredients',
    )
    fields = ('name', 'ingredients', 'instructions')


@admin.register(CocktailIngredient)
class CocktailIngredientAdmin(AutocompleteAdmin):
    ordering = ('ingredient__name',)
    fields = ('ingredient', 'amount', 'measurement', 'preparation',)
    autocomplete_fields = ('ingredient',)
    search_fields = ('ingredient__name',)


@admin.register(Ingredient)
class IngredientAdmin(AutocompleteAdmin):
    # form = IngredientForm
    search_fields = (
        'name',
        'is_controlled',
    )
    fields = ('name', 'is_controlled',)

@admin.register(Feast)
class FeastAdmin(AutocompleteAdmin):
    # form = FeastForm
    search_fields = (
        'name',
    )
    list_filter = ('_date',)
    ordering = ('_date',)
    fields = ('_date', 'name', 'cocktails', 'ext_calapi_inadiutorium_season', 'ext_calapi_inadiutorium_celebration',)
    autocomplete_fields = ('cocktails', 'ext_calapi_inadiutorium_celebration',)


@admin.register(ControlledBeverage)
class ControlledBeverageAdmin(AutocompleteAdmin):
    # form = ControlledBeverageForm
    search_fields = (
        'name',
    )
    fields = ('name', 'ingredients', 'is_in_stock',)
    autocomplete_fields = ('ingredients',)
