from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Staff'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)


class Member(models.Model):
    nid = models.IntegerField(primary_key=True)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    birth_date = models.DateField()
    phone = models.IntegerField()
    first_dose_date = models.DateField(blank=True, null=True)
    first_dose_done = models.BooleanField(default=False)
    second_dose_date = models.DateField(blank=True, null=True)
    second_dose_done = models.BooleanField(default=False)
    HOSPITAL_CHOICES = (
        (1, 'Dhaka Medical College Hospital'),
        (2, 'Delta Medical College'),
    )
    hospital_choice = models.PositiveSmallIntegerField(choices=HOSPITAL_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.nid} : {self.first_name}"


class Staff(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = models.Manager()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(user=instance)
        if instance.user_type == 2:
            Staff.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staff.save()
