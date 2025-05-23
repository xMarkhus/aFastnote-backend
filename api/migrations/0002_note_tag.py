# Generated by Django 5.1.5 on 2025-03-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="tag",
            field=models.CharField(
                choices=[
                    ("urgente", "Urgente"),
                    ("estudo", "Estudo"),
                    ("ideia", "Ideia"),
                    ("projeto", "Projeto"),
                    ("financeiro", "Financeiro"),
                    ("pessoal", "Pessoal"),
                    ("trabalho", "Trabalho"),
                    ("lazer", "Lazer"),
                    ("saude", "Saúde"),
                    ("eventos", "Eventos"),
                ],
                default="pessoal",
                max_length=20,
            ),
        ),
    ]
