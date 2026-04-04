from django.db import models

class Person(models.Model):
    modalities = [('online','Online'), ('face2face', 'Face2Face'), ('mix', 'Mix')]
    experiences_badges = [('adventurer', 'Adventurer'), ('experienced', 'Experienced'), ('hero', 'Hero')]
    #part 1 -----------------------------
    name = models.CharField(max_length=42)
    mail = models.CharField(max_length=46, primary_key=True, unique=True)
    phone = models.IntegerField(max_length=9)
    #part 2 -----------------------------
    experience = models.CharField(choices=experiences_badges)
    dnd = models.BooleanField(default=False)
    pathfinder = models.BooleanField(default=False)
    cthulhu = models.BooleanField(default=False)
    indie = models.BooleanField(default=False)
    others = models.BooleanField(default=False)
    none = models.BooleanField(default=False)
    #part 3 -----------------------------
    interests = models.TextField()
    modality = models.CharField(choices=modalities)
    #part 4 -----------------------------
    first_term = models.BooleanField(default=False)
    second_term = models.BooleanField(default=False)



