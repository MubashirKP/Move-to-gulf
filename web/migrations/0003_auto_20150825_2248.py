# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_posted_jobs_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posted_jobs',
            name='company_logo',
            field=models.ImageField(null=True, upload_to=b'/static/uploads/companylogo/', blank=True),
        ),
    ]
