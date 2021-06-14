from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password, is_staff, is_superuser, is_active, **other_fields):
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, email, password=None, **other_fields):
        return self._create_user(email, password, False, False, False, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        return self._create_user(email, password, True, True, True, **other_fields)

    def validation_code(self, user_id, code):
        if self.filter(id = user_id, confirm_code = code).exists():
            return True
        else:
            return False