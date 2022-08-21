from django.db import models


# Create your models here.
class Account(models.Model):
    steamid = models.CharField(max_length=255, unique=True)
    communityvisibilitystate = models.IntegerField(null=True)
    profilestate = models.IntegerField(null=True)
    personaname = models.CharField(max_length=255)
    profileurl = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    avatarmedium = models.CharField(max_length=255)
    avatarfull = models.CharField(max_length=255)
    avatarhash = models.CharField(max_length=255)
    lastlogoff = models.DateTimeField(null=True)
    personastate = models.IntegerField(null=True)
    primaryclanid = models.CharField(max_length=255)
    timecreated = models.DateTimeField(null=True)
    personastateflags = models.IntegerField(null=True)
    loccountrycode = models.CharField(max_length=255)

    def __str__(self):
        return self.personaname
