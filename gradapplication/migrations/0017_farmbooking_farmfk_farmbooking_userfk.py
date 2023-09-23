# Generated by Django 4.2.5 on 2023-09-22 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gradapplication', '0016_publicplace_userfk_alter_publicplace_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmbooking',
            name='FarmFK',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.farm'),
        ),
        migrations.AddField(
            model_name='farmbooking',
            name='userFK',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.user'),
        ),
    ]
