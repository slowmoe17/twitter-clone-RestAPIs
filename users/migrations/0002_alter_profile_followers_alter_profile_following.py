# Generated by Django 4.0.5 on 2022-06-10 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, default=0, related_name='followers', to='users.user'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='users.user'),
        ),
    ]
