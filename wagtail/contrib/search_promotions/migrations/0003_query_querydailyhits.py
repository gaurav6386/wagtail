# Generated by Django 3.1.8 on 2021-06-22 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_string', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='QueryDailyHits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hits', models.IntegerField(default=0)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_hits', to='wagtailsearchpromotions.query')),
            ],
            options={
                'verbose_name': 'Query Daily Hits',
                'verbose_name_plural': 'Query Daily Hits',
                'unique_together': {('query', 'date')},
            },
        ),
    ]
