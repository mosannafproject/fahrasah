# Generated by Django 4.2 on 2023-12-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrasah', '0010_field_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='property',
            field=models.CharField(blank=True, choices=[('جدول', 'Table'), ('نص', 'Text'), ('مذكرة', 'Memo'), ('رقم', 'Number'), ('عملة', 'Currency'), ('ترقيم تلقائي', 'Auto Number'), ('منطقية', 'Boolean'), ('كائن', 'Object'), ('نسبة مئوية', 'Percentage'), ('حاسبة', 'Calculator')], max_length=200, null=True, verbose_name='خصائص الحقل'),
        ),
    ]
