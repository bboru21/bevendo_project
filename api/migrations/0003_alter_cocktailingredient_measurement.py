# Generated by Django 3.2.9 on 2021-11-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_feast_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailingredient',
            name='measurement',
            field=models.CharField(blank=True, choices=[('bottle', 'bottle'), ('broken in half', 'broken in half'), ('chopped canned', 'chopped canned'), ('cube', 'cube'), ('cup', 'cup'), ('dash', 'dash'), ('drop', 'drop'), ('hollowed out', 'hollowed out'), ('leaf', 'leaf'), ('liter', 'liter'), ('jigger', 'jigger'), ('ounce', 'ounce'), ('part', 'part'), ('peel', 'peel'), ('pint', 'pint'), ('scoop', 'scoop'), ('slice', 'slice'), ('splash', 'splash'), ('spiral', 'spiral'), ('sprig', 'sprig'), ('sprinkle', 'sprinkle'), ('stalk', 'stalk'), ('tablespoon', 'tablespoon'), ('teaspoon', 'teaspoon'), ('thinly sliced', 'thinly sliced'), ('twist', 'twist'), ('wedge', 'wedge'), ('wheel', 'wheel'), ('white', 'white'), ('yolk', 'yolk'), ('zest', 'zest')], default=None, max_length=20, null=True),
        ),
    ]