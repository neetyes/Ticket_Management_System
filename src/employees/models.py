from django.db import models

# Create your models here.
class Employee(models.Model):
    name        = models.CharField(max_length=254)
    mobile      = models.CharField(max_length=254, null=True, blank=True)
    email       = models.EmailField(max_length=254, null=True, blank=True, unique=True)
    position    = models.CharField(max_length=254, null=True, blank=True)
    picture     = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name