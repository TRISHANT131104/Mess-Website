# Generated by Django 4.1.7 on 2023-05-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_unregisteredstudent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unregisteredstudent',
            options={'verbose_name': 'Unregistered Students', 'verbose_name_plural': 'Unregistered Students'},
        ),
        migrations.RemoveField(
            model_name='longrebate',
            name='allocation_id_id',
        ),
        migrations.RemoveField(
            model_name='longrebate',
            name='month',
        ),
        migrations.AddField(
            model_name='longrebate',
            name='end_date',
            field=models.DateField(blank=True, help_text='end date of the rebate', null=True),
        ),
        migrations.AddField(
            model_name='longrebate',
            name='start_date',
            field=models.DateField(blank=True, help_text='start date of the rebate', null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(blank=True, help_text='This contains phone number of the contact to be added', max_length=12, null=True, verbose_name='Phone Number'),
        ),
    ]