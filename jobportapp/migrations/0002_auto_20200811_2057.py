# Generated by Django 3.0.8 on 2020-08-11 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clgdet',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobportapp.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='othdet',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobportapp.profile'),
            preserve_default=False,
        ),
    ]
