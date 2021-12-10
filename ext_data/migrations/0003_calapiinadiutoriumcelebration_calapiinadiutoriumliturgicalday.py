# Generated by Django 3.2.9 on 2021-11-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ext_data', '0002_auto_20211116_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalapiInadiutoriumCelebration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create_date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified_date')),
                ('title', models.CharField(max_length=500, null=True)),
                ('colour', models.CharField(choices=[('green', 'Green'), ('violet', 'Violet'), ('white', 'White'), ('red', 'Red')], max_length=6)),
                ('rank', models.CharField(max_length=255)),
                ('rank_num', models.FloatField()),
            ],
            options={
                'ordering': ('rank_num',),
            },
        ),
        migrations.CreateModel(
            name='CalapiInadiutoriumLiturgicalDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create_date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='modified_date')),
                ('date', models.DateField()),
                ('season', models.CharField(choices=[('ordinary', 'Ordinary Time'), ('advent', 'Advent'), ('christmas', 'Christmas'), ('lent', 'Lent'), ('easter', 'Easter')], max_length=9)),
                ('season_week', models.IntegerField()),
                ('weekday', models.CharField(choices=[('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')], max_length=9)),
                ('celebrations', models.ManyToManyField(related_name='liturgical_days', to='ext_data.CalapiInadiutoriumCelebration')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]