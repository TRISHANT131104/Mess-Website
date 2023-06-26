# Generated by Django 4.2.2 on 2023-06-26 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_leftshortrebate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sno', models.IntegerField(default=0, help_text='This contains the serial number of the Period', verbose_name='Sno')),
                ('start_date', models.DateField(blank=True, help_text='This contains the start date of this Period for this semester', null=True)),
                ('end_date', models.DateField(blank=True, help_text='This contains the end date of this Period of this semester', null=True)),
            ],
            options={
                'verbose_name': 'Period Details',
                'verbose_name_plural': 'Period Details',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, help_text='Name of the semester', max_length=30, null=True, verbose_name='Semester Name')),
            ],
        ),
        migrations.CreateModel(
            name='StudentBills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period1_short', models.IntegerField(default=0, null=True, verbose_name='Period 1 Short')),
                ('period1_long', models.IntegerField(default=0, null=True, verbose_name='Period 1 Long')),
                ('period1_high_tea', models.BooleanField(default=True, null=True, verbose_name='Period 1 High Tea')),
                ('period1_bill', models.IntegerField(default=0, null=True, verbose_name='Period 1 Rebate Amount')),
                ('period2_short', models.IntegerField(default=0, null=True, verbose_name='Period 2 Short')),
                ('period2_long', models.IntegerField(default=0, null=True, verbose_name='Period 2 Long')),
                ('period2_high_tea', models.BooleanField(default=True, null=True, verbose_name='Period 2 High Tea')),
                ('period2_bill', models.IntegerField(default=0, null=True, verbose_name='Period 2 Rebate Amount')),
                ('period3_short', models.IntegerField(default=0, null=True, verbose_name='Period 3 Short')),
                ('period3_long', models.IntegerField(default=0, null=True, verbose_name='Period 3 Long')),
                ('period3_high_tea', models.BooleanField(default=True, null=True, verbose_name='Period 3 High Tea')),
                ('period3_bill', models.IntegerField(default=0, null=True, verbose_name='Period 3 Rebate Amount')),
                ('period4_short', models.IntegerField(default=0, null=True, verbose_name='Period 4 Short')),
                ('period4_long', models.IntegerField(default=0, null=True, verbose_name='Period 4 Long')),
                ('period4_high_tea', models.BooleanField(default=True, null=True, verbose_name='Period 4 High Tea')),
                ('period4_bill', models.IntegerField(default=0, null=True, verbose_name='Period 4 Rebate Amount')),
                ('period5_short', models.IntegerField(default=0, null=True, verbose_name='Period 5 Short')),
                ('period5_long', models.IntegerField(default=0, null=True, verbose_name='Period 5 Long')),
                ('period5_high_tea', models.BooleanField(default=True, null=True, verbose_name='Period 5 High Tea')),
                ('period5_bill', models.IntegerField(default=0, null=True, verbose_name='Period 5 Rebate Amount')),
                ('period6_short', models.IntegerField(default=0, null=True, verbose_name='Period 6 Short')),
                ('period6_long', models.IntegerField(default=0, null=True, verbose_name='Period 6 Long')),
                ('period6_high_tea', models.BooleanField(default=True, null=True, verbose_name='Period 6 High Tea')),
                ('period6_bill', models.IntegerField(default=0, null=True, verbose_name='Period 6 Rebate Amount')),
                ('email', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.student')),
                ('period', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.period', verbose_name='Period')),
            ],
            options={
                'verbose_name': 'Rebate Bill',
                'verbose_name_plural': 'Rebate Bills',
            },
        ),
        migrations.AddField(
            model_name='period',
            name='semester',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.semester', verbose_name='Semester'),
        ),
        migrations.CreateModel(
            name='CatererBills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period1_bills', models.IntegerField(default=0, null=True, verbose_name='Period 1 Bill')),
                ('period2_bills', models.IntegerField(default=0, null=True, verbose_name='Period 2 Bill')),
                ('period3_bills', models.IntegerField(default=0, null=True, verbose_name='Period 3 Bill')),
                ('period4_bills', models.IntegerField(default=0, null=True, verbose_name='Period 4 Bill')),
                ('period5_bills', models.IntegerField(default=0, null=True, verbose_name='Period 5 Bill')),
                ('period6_bills', models.IntegerField(default=0, null=True, verbose_name='Period 6 Bill')),
                ('caterer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.caterer')),
                ('period', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.period', verbose_name='Period')),
            ],
            options={
                'verbose_name': 'Caterer Bill',
                'verbose_name_plural': 'Caterer Bills',
            },
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, default=None, help_text='This contains the Allocation Id', max_length=30, null=True, verbose_name='Allocation Id')),
                ('high_tea', models.BooleanField(blank=True, default=False, help_text='This contains the info if high tea is taken or not', null=True, verbose_name='High Tea')),
                ('first_pref', models.CharField(blank=True, default=None, help_text='This contians the first preference caterer of the student', max_length=10, null=True, verbose_name='First Preference')),
                ('second_pref', models.CharField(blank=True, default=None, help_text='This contians the first preference caterer of the student', max_length=10, null=True, verbose_name='Second Preference')),
                ('third_pref', models.CharField(blank=True, default=None, help_text='This contians the first preference caterer of the student', max_length=10, null=True, verbose_name='Third Preference')),
                ('caterer', models.ForeignKey(default=None, help_text='Contains the allocated caterer of the student', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.caterer')),
                ('email', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.student')),
                ('month', models.ForeignKey(default=None, help_text='Contains the period of allocation', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.period')),
            ],
            options={
                'verbose_name': 'Allocation Detail',
                'verbose_name_plural': 'Allocation Details',
            },
        ),
    ]
