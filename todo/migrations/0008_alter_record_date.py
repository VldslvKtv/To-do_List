# Generated by Django 4.2.4 on 2023-09-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_record_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(editable=False, null=True),
        ),
    ]
