# Generated by Django 4.1 on 2022-09-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="tipo",
            field=models.CharField(
                choices=[("V", "Variavel"), ("S", "Simples")], default="V", max_length=1
            ),
        ),
    ]
