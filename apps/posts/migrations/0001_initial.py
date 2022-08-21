# Generated by Django 4.0.5 on 2022-07-09 17:43

import apps.posts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=160, unique=True)),
                ('tag_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('about', models.TextField()),
            ],
            options={
                'db_table': 'tag',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=180, unique=True)),
                ('thumbnail', models.ImageField(upload_to=apps.posts.models.upload_thumbnail_to)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published'), ('SP', 'Suspended'), ('UN', 'Unpublished')], default='DR', max_length=2)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='posts.tag')),
            ],
            options={
                'db_table': 'post',
                'ordering': ['-created_at'],
                'permissions': [('can_publish_a_post', 'Can publish a post'), ('can_mark_post_as_featured', 'Can mark post as featured')],
                'abstract': False,
            },
        ),
    ]