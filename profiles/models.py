from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='default_profile.png'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile, image is {self.image}"

# Automatically create a Profile instance when a new user is created


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

# Automatically save the Profile when the User instance is saved


def save_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)
