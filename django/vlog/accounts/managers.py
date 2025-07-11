from django.contrib.auth.base_user import BaseUserManager
"""
customize user for my convenion
"""
class customUsermanager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Enter valid email id")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if not extra_fields.get("is_staff"):
            raise ValueError("superuser must have staff access")
        if not extra_fields.get("is_superuser"):
            raise ValueError("superuser must have superuser access")
        return self.create_user(email, password, **extra_fields)

