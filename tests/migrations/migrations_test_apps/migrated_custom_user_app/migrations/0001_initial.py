# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    operations = [

        migrations.CreateModel(
            "SillyUser",
            [
                ("id", models.AutoField(primary_key=True)),
                ("email", models.EmailField()),
                ("password", models.CharField()),
                ("hates_tribbles", models.BooleanField(default=True)),
            ]
        ),

        migrations.CreateModel(
            "Tribble",
            [
                ("id", models.AutoField(primary_key=True)),
                ("fluffy", models.BooleanField(default=True)),
            ],
        )

    ]
