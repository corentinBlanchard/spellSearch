from django.db import models

class Classes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Monster(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Sorts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    spell_resistance = models.BooleanField(default=False)
    is_verbal = models.BooleanField(default=False)
    is_somatic = models.BooleanField(default=False)
    is_material = models.BooleanField(default=False)
    classes = models.ManyToManyField(Classes)
    max_level = models.IntegerField(default=0)
    monsters = models.ManyToManyField(Monster)