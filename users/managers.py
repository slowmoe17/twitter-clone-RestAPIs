from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, phone, gender, name,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email or phone :
            raise ValueError("Users must have an email address or phone number")

        user = self.model(
            email=self.normalize_email(email), username=username, gender=gender, phone=phone,name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,username, phone, gender, password):
        """Create and save a new superuser with given details"""

        user = self.create_user(email, username, phone,name, gender, password)

        user.admin = True
        user.staff = True

        user.save(using=self._db)
        return user