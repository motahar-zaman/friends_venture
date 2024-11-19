from django.db import models
from .main import BaseModel
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import JSONField


class Partner(BaseModel):
    first_name = models.CharField(db_column='FirstName', max_length=64)
    last_name = models.CharField(db_column='LastName', max_length=64, null=True)
    nick_name = models.CharField(db_column='UserName', max_length=64)
    date_of_birth = models.DateField(db_column='DateOfBirth', null=True, blank=True)
    email = models.EmailField(db_column='PrimaryEmail', max_length=64, null=True)
    phone_number = models.CharField(db_column='PhoneNumber', max_length=16, null=True)
    alternate_contact_number = models.CharField(db_column='AlternateContactNumber', max_length=16, null=True)
    address = models.TextField(db_column='Address', null=True)
    note = models.TextField(db_column='Note', null=True)
    missing_info = JSONField(DjangoJSONEncoder, db_column='MissingInfo', null=True, default=dict)

    def __str__(self):
        return self.nick_name

    class Meta:
        ordering = ['-created_at']
        db_table = 'Partner'
