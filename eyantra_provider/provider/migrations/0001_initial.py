# Generated by Django 3.0.7 on 2020-06-07 09:42

import authlib.oauth2.rfc6749.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import provider.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuth2Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, max_length=48)),
                ('token_type', models.CharField(max_length=40)),
                ('access_token', models.CharField(max_length=255, unique=True)),
                ('refresh_token', models.CharField(db_index=True, max_length=255)),
                ('scope', models.TextField(default='')),
                ('revoked', models.BooleanField(default=False)),
                ('issued_at', models.IntegerField(default=provider.models.now_timestamp)),
                ('expires_in', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, authlib.oauth2.rfc6749.models.TokenMixin),
        ),
        migrations.CreateModel(
            name='OAuth2Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, max_length=48, unique=True)),
                ('client_secret', models.CharField(blank=True, max_length=48)),
                ('client_name', models.CharField(max_length=120)),
                ('redirect_uris', models.TextField(default='')),
                ('default_redirect_uri', models.TextField(default='')),
                ('scope', models.TextField(default='')),
                ('response_type', models.TextField(default='')),
                ('grant_type', models.TextField(default='')),
                ('token_endpoint_auth_method', models.CharField(default='', max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, authlib.oauth2.rfc6749.models.ClientMixin),
        ),
        migrations.CreateModel(
            name='AuthorizationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, max_length=48)),
                ('code', models.CharField(max_length=120, unique=True)),
                ('redirect_uri', models.TextField(default='', null=True)),
                ('response_type', models.TextField(default='')),
                ('scope', models.TextField(default='', null=True)),
                ('auth_time', models.IntegerField(default=provider.models.now_timestamp)),
                ('nonce', models.CharField(default='', max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, authlib.oauth2.rfc6749.models.AuthorizationCodeMixin),
        ),
    ]
