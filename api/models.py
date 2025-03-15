from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    TAG_CHOICES = [
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
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(
        max_length=20,
        choices=TAG_CHOICES,
        default="pessoal"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
