# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(to='main.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
