# Generated by Django 4.2 on 2023-04-16 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fahrasah', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم قاعدة البيانات')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='اسم المشروع')),
                ('start_date', models.DateTimeField(verbose_name='تاريخ بداية المشروع')),
                ('end_date', models.DateTimeField(verbose_name='الموعد النهائي المتوقع')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم الصفحة')),
                ('reference', models.CharField(max_length=200, verbose_name='مرجع الصفحة')),
                ('url', models.URLField(verbose_name='رابط الصفحة')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fahrasah.project', verbose_name='المشروع')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم الحقل')),
                ('description', models.CharField(max_length=255, verbose_name='وصف الحقل')),
                ('reference', models.CharField(max_length=200, verbose_name='مرجع الحقل')),
                ('url', models.URLField(blank=True, null=True, verbose_name='رابط الحقل')),
                ('cmd', models.CharField(max_length=255, verbose_name='سطر الأمر')),
                ('database', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fahrasah.database')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fahrasah.page', verbose_name='الصفحة')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fahrasah.project')),
            ],
        ),
    ]
