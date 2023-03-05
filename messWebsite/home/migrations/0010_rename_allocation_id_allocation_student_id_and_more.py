# Generated by Django 4.1.7 on 2023-03-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_allocation_student_scan_rebate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allocation',
            old_name='allocation_id',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='scan',
            old_name='allocation_id',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='allocation_id',
            new_name='student_id',
        ),
        migrations.AlterField(
            model_name='scan',
            name='breakfast',
            field=models.BooleanField(help_text='This contains if the breeakfast was eaten by the student', verbose_name='Breakfast'),
        ),
        migrations.AlterField(
            model_name='scan',
            name='dinner',
            field=models.BooleanField(help_text='This contains if the dinner was eaten by the student', verbose_name='dinner'),
        ),
        migrations.AlterField(
            model_name='scan',
            name='high_tea',
            field=models.BooleanField(help_text='This contains if the high tea was eaten by the student', verbose_name='high_tea'),
        ),
        migrations.AlterField(
            model_name='scan',
            name='lunch',
            field=models.BooleanField(help_text='This contains if the lunch was eaten by the student', verbose_name='lunch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(help_text='This contains the roll number of the Student', max_length=10, verbose_name='Roll number of Student'),
        ),
    ]
