# Generated by Django 4.1.2 on 2022-10-27 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='Artiste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artiste',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
    ]
