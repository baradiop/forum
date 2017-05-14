from django.db import models
from django.utils import timezone

class Post(models.Model):
    auteur=models.ForeignKey('auth.User')
    titre=models.CharField(max_length=200)
    texte=models.TextField()
    date_creation=models.DateTimeField(default=timezone.now)
    date_pub=models.DateTimeField(blank=True,null=True)

    def publier(self):
        self.date_pub=timezone.now()
        self.save()

    def __str__(self):
        return self.titre
