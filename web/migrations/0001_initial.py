# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Posted_Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_email', models.EmailField(max_length=70)),
                ('job_title', models.CharField(max_length=256)),
                ('job_desc', models.TextField()),
                ('job_url', models.CharField(max_length=256, null=True)),
                ('job_expiring', models.DateField()),
                ('job_company_name', models.CharField(max_length=256)),
                ('company_logo', models.ImageField(upload_to=b'/static/uploads/companylogo/')),
                ('job_category', models.ForeignKey(to='web.Job_Category')),
                ('job_location', models.ForeignKey(to='web.Job_Location')),
                ('job_type', models.ForeignKey(to='web.Job_Type')),
            ],
        ),
    ]
