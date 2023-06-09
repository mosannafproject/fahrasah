# Generated by Django 4.2 on 2023-04-25 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fahrasah', '0002_database_project_page_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='اسم المجال')),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='اسم النشاط')),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='اسم الحقل')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='website_name',
            field=models.CharField(default='', max_length=200, verbose_name='اسم الموقع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='website_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fahrasah.websiteactivity'),
        ),
        migrations.AddField(
            model_name='project',
            name='website_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fahrasah.websitefield'),
        ),
    ]
