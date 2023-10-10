# Generated by Django 4.1.4 on 2023-04-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('TD', 'To Do'), ('IP', 'In Progress'), ('DN', 'Done')], max_length=2)),
            ],
        ),
    ]