# Generated by Django 3.1.1 on 2020-09-30 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_auto_20200930_0926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendas',
            options={'permissions': (('setar_nfe', 'Usuario pode alterar parametro NF-e'), ('ver_dashboard', 'Pode vizualizar o dashboard'), ('permissao3', 'permissao3'))},
        ),
    ]