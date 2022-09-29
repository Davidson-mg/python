# Generated by Django 4.1 on 2022-09-11 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='conteudo_post',
            field=models.TextField(verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerto_post',
            field=models.TextField(verbose_name='Excerto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem_post',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado_post',
            field=models.BooleanField(default=False, verbose_name='Publicado '),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo_post',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]
