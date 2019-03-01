from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=None)
    birth = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=11, null=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name_plural = '个性化用户信息'

    def __str__(self):
        return self.user.username

class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=None)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)

    class Meta:
        db_table = 'user_info'

    def __str__(self):
        return self.user.username



