# Generated by Django 5.0.8 on 2024-10-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrscan', '0002_meal_high_tea'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessTimings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('high_tea', 'High Tea'), ('dinner', 'Dinner')], help_text='This contains the meal type', max_length=10)),
                ('start_time', models.TimeField(blank=True, help_text='This contains the start time', null=True)),
                ('end_time', models.TimeField(blank=True, help_text='This contains the end time', null=True)),
            ],
        ),
    ]