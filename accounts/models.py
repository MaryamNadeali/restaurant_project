from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.utils.translation import gettext as _
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.PositiveIntegerField(_("شماره همراه"),null=True,blank=True)