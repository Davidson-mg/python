# Generated by Django 4.1 on 2022-10-12 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("principal", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tarefa",
            name="codigo",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tarefa",
            name="previsao_conclusao",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="tarefa",
            name="usuario",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
    ]
