# Generated by Django 4.1.2 on 2022-10-30 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_tag_remove_project_tags_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Tags',
            field=models.ManyToManyField(blank=True, related_name='project', to='projects.tag'),
        ),
    ]
