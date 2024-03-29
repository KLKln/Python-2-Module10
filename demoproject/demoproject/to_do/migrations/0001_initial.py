# Generated by Django 3.2.8 on 2021-10-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='to_do_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_added', models.CharField(max_length=200)),
                ('who_assigned', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(verbose_name='created date')),
                ('to_do_name', models.CharField(max_length=500)),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('completed', models.IntegerField(default=0)),
            ],
        ),
    ]
