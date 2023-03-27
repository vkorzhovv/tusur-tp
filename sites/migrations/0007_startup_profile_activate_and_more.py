# Generated by Django 4.1.4 on 2022-12-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_startup_profile_ceo_team_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup_profile',
            name='activate',
            field=models.BooleanField(blank=True, default=False, verbose_name='Прошел модерацию?'),
        ),
        migrations.AlterField(
            model_name='startup_profile',
            name='presentation',
            field=models.FileField(blank=True, null=True, upload_to='users/StartUp_Profile/presentation', verbose_name='Презентация'),
        ),
    ]