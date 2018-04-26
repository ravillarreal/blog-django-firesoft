# Generated by Django 2.0.4 on 2018-04-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_image', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
