# Generated by Django 3.0.6 on 2020-09-07 04:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_thumbnail', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpg', force_format='JPEG', keep_meta=False, quality=90, size=[900, 600], upload_to='posts_image')),
                ('tags', models.CharField(blank=True, max_length=60, validators=[django.core.validators.RegexValidator('^[, a-zA-Z]*$', 'Enter comma separated tags. (use space for two words tag)')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('featured', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='posts.Category')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
