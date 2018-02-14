# Generated by Django 2.0.2 on 2018-02-11 09:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
