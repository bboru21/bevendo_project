# Generated by Django 3.2.6 on 2021-08-24 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('instructions', models.TextField(blank=None, default=None, null=True)),
            ],
            options={
                'db_table': 'api_cocktail',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_controlled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'api_ingredient',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Feast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=250)),
                ('cocktails', models.ManyToManyField(blank=True, default=None, to='api.Cocktail')),
            ],
            options={
                'db_table': 'api_feast',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ControlledBeverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_in_stock', models.BooleanField(default=False, null=True)),
                ('ingredients', models.ManyToManyField(blank=True, default=None, to='api.Ingredient')),
            ],
            options={
                'verbose_name': 'Controlled Beverage',
                'verbose_name_plural': 'Controlled Beverages',
                'db_table': 'api_controlledbeverage',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CocktailIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True)),
                ('measurement', models.CharField(blank=True, choices=[('broken in half', 'broken in half'), ('chopped canned', 'chopped canned'), ('cube', 'cube'), ('cup', 'cup'), ('dash', 'dash'), ('drop', 'drop'), ('hollowed out', 'hollowed out'), ('leaf', 'leaf'), ('liter', 'liter'), ('jigger', 'jigger'), ('ounce', 'ounce'), ('part', 'part'), ('peel', 'peel'), ('pint', 'pint'), ('scoop', 'scoop'), ('slice', 'slice'), ('splash', 'splash'), ('spiral', 'spiral'), ('sprig', 'sprig'), ('sprinkle', 'sprinkle'), ('stalk', 'stalk'), ('tablespoon', 'tablespoon'), ('teaspoon', 'teaspoon'), ('thinly sliced', 'thinly sliced'), ('twist', 'twist'), ('wedge', 'wedge'), ('wheel', 'wheel'), ('white', 'white'), ('yolk', 'yolk'), ('zest', 'zest')], default=None, max_length=20, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ingredient')),
            ],
            options={
                'verbose_name': 'Cocktail Ingredient',
                'verbose_name_plural': 'Cocktail Ingredients',
                'db_table': 'api_cocktailingredient',
                'ordering': [],
            },
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ingredients',
            field=models.ManyToManyField(to='api.CocktailIngredient'),
        ),
    ]
