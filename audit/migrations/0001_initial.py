# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accession_no', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_shelves', models.IntegerField()),
                ('total_books', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('shelf_no', models.IntegerField(serialize=False, primary_key=True)),
                ('row_1', models.IntegerField(default=0)),
                ('row_2', models.IntegerField(default=0)),
                ('row_3', models.IntegerField(default=0)),
                ('book_file', models.FileField(upload_to=b'')),
            ],
            options={
                'ordering': ['shelf_no'],
            },
        ),
        migrations.CreateModel(
            name='TagError',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('error_type', models.CharField(max_length=1, choices=[(b'W', b'Weak Tag'), (b'N', b'No Tag'), (b'M', b'Multiple Tags'), (b'O', b'Other')])),
                ('corrected', models.BooleanField(default=b'FALSE')),
                ('book', models.ForeignKey(to='audit.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='shelf',
            field=models.ForeignKey(to='audit.Shelf'),
        ),
    ]
