from django.db import models
from .main import BaseModel
import uuid
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import JSONField
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):
    # id = models.UUIDField(db_column='UserID', primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(db_column='FirstName', max_length=64)
    last_name = models.CharField(db_column='LastName', max_length=64, null=True)
    username = models.CharField(db_column='UserName', unique=True, max_length=64, null=True)
    password = models.CharField(db_column='Password', max_length=256, null=True)
    email = models.EmailField(db_column='PrimaryEmail', max_length=256, null=True)
    primary_contact_number = models.CharField(db_column='PrimaryContactNumber', max_length=16, null=True)

    db_context = JSONField(DjangoJSONEncoder, null=True, default=dict)
    is_active = models.BooleanField(db_column='IsActive', default=True)
    mfa_enabled = models.BooleanField(db_column='MFAEnabled', default=False)
    custom_roles = ArrayField(models.UUIDField(), default=list, null=True, blank=True)
    secret_key = models.CharField(db_column='SecretKey', max_length=32, null=True, blank=True)
    access_token = models.CharField(db_column='AccessToken', max_length=64, null=True, blank=True)
    access_token_time = models.DateTimeField(db_column='AccessTokenTime', null=True, blank=True)

    user_type = models.CharField(db_column='UserType', max_length=64, null=True, blank=True)
    address = models.CharField(db_column='Address', max_length=256, null=True, blank=True)
    note = models.CharField(db_column='Note', max_length=512, null=True, blank=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username}'

    class Meta:
        db_table = 'User'
