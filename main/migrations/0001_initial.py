# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('author', models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=16, null=True, blank=True)),
                ('about_me', models.CharField(max_length=200, null=True, blank=True)),
                ('location', models.CharField(max_length=64, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='follows',
            name='followed',
            field=models.ForeignKey(related_name='followed', to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follows',
            name='follower',
            field=models.ForeignKey(related_name='followers', to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='follows',
            unique_together=set([('follower', 'followed')]),
        ),
    ]
