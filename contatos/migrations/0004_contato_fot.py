# Generated by Django 5.0 on 2023-12-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_rename_mostra_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='fot',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
