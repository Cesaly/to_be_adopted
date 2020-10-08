# Generated by Django 3.1.2 on 2020-10-08 06:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
                ('pet_type', models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat')], default='DOG', max_length=3)),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
                ('bio', models.TextField()),
                ('spay_neuter', models.BooleanField(default=False)),
                ('shot_record', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, choices=[(1, 'Up For Adoption'), (2, 'Adopted')], default=1, max_length=2)),
                ('pet_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]