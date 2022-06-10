from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
class User(AbstractBaseUser):
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=20 , unique=True)
    gender = models.CharField(max_length=1,choices=genders)
    phone = models.CharField(max_length=20, blank=True, null=True,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "gender","phone"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email + " | " + self.username + " | " + self.name + " | " + self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True ,default=0)
    following = models.ForeignKey(User, related_name='following', blank=True, null=True, on_delete=models.CASCADE , default=0)


