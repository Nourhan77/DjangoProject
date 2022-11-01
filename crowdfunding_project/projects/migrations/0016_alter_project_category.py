# Generated by Django 4.1.2 on 2022-10-31 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Infrastucture', 'Infrastucture'), ('Development', 'Development'), ('Product', 'Product')], max_length=100, null=True),
        ),
    ]