# Generated by Django 3.0.4 on 2020-03-29 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0016_auto_20200328_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='provider_type',
            field=models.IntegerField(choices=[(0, 'Unknown'), (1, 'Other'), (2, 'Doctor'), (3, 'Nurse'), (4, 'Student')], default=0, help_text='Doctor, nurse or student', verbose_name='Provider type'),
        ),
    ]
