# Generated by Django 4.1 on 2022-08-10 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCatena', '0003_alter_operacao_funcionarioresp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comarca',
            options={'ordering': ['nome']},
        ),
    ]
