# Generated by Django 3.2.6 on 2021-08-23 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Период',
                'verbose_name_plural': 'Периоды',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField(max_length=200)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='views_works.period')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ['published'],
            },
        ),
    ]
