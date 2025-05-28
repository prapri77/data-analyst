from django.contrib.auth.base_user import BaseUserManager

"""
to customize the saving format of my user from accoutns app
"""


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("enter the valid email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fiedls):
        extra_fiedls.setdefault("is_staff", True)
        extra_fiedls.setdefault("is_superuser", True)
        if not extra_fiedls.get("is_staff"):
            raise ValueError("superuser must have staff access")
        if not extra_fiedls.get("is_superuser"):
            raise ValueError("superuser must have superuser access")
        return self.create_user(email, password, **extra_fiedls)
