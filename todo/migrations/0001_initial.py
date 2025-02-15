# Generated by Django 4.2.4 on 2023-09-12 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('important', models.BooleanField(default=False)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('n', 'NOT_ACTIVE'), ('p', 'PROGRESS'), ('c', 'COMPLETED')], default=('p', 'PROGRESS'), max_length=1)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
