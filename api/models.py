from django.db import models
from django.contrib.humanize.templatetags.humanize import ordinal

INGREDIENT_MEASUREMENTS = (
    ('broken in half', 'broken in half'),
    ('chopped canned', 'chopped canned'),
    ('cube', 'cube'),
    ('cup', 'cup'),
    ('dash', 'dash'),
    ('drop', 'drop'),
    ('hollowed out', 'hollowed out'),
    ('leaf', 'leaf'),
    ('liter', 'liter'),
    ('jigger', 'jigger'),
    ('ounce', 'ounce'),
    ('part', 'part'),
    ('peel', 'peel'),
    ('pint', 'pint'),
    ('scoop', 'scoop'),
    ('slice', 'slice'),
    ('splash', 'splash'),
    ('spiral', 'spiral'),
    ('sprig', 'sprig'),
    ('sprinkle', 'sprinkle'),
    ('stalk', 'stalk'),
    ('tablespoon', 'tablespoon'),
    ('teaspoon', 'teaspoon'),
    ('thinly sliced', 'thinly sliced'),
    ('twist', 'twist'),
    ('wedge', 'wedge'),
    ('wheel', 'wheel'),
    ('white', 'white'),
    ('yolk', 'yolk'),
    ('zest', 'zest'),
)

'''
    Helpful here: Would you buy it at the store? If so, it's an ingredient. If
    not, it's probably made from an Ingredient.
'''


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    is_controlled = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        app_label = 'api'
        db_table = 'api_ingredient'

    def __str__(self):
        return f'{self.name} ({self.id})'


class ControlledBeverage(models.Model):
    name = models.CharField(max_length=250)
    ingredients = models.ManyToManyField(Ingredient, default=None, blank=True)
    is_in_stock = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        ordering = ['name']
        verbose_name = 'Controlled Beverage'
        verbose_name_plural = 'Controlled Beverages'
        app_label = 'api'
        db_table = 'api_controlledbeverage'


class CocktailIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default=None
    )
    measurement = models.CharField(
        max_length=20,
        choices=INGREDIENT_MEASUREMENTS,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f'{self.ingredient.name} ({self.amount} {self.measurement})'

    class Meta:
        ordering = []
        verbose_name = 'Cocktail Ingredient'
        verbose_name_plural = 'Cocktail Ingredients'
        app_label = 'api'
        db_table = 'api_cocktailingredient'


class Cocktail(models.Model):
    name = models.CharField(max_length=250)
    ingredients = models.ManyToManyField(CocktailIngredient)
    instructions = models.TextField(null=True, blank=None, default=None)

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        ordering = ['name']
        app_label = 'api'
        db_table = 'api_cocktail'


class Feast(models.Model):
    date = models.DateField(
        blank=True,     # admin
        null=True,      # database
    )
    name = models.CharField(max_length=250)
    cocktails = models.ManyToManyField(Cocktail, default=None, blank=True)

    def __str__(self):
        _str = f"{self.name} ({self.id})"
        if self.date:
            _str = f"{self.date.strftime('%B')} {ordinal(self.date.day)} - {_str}"
        return _str

    class Meta:
        ordering = ['date']
        app_label = 'api'
        db_table = 'api_feast'
