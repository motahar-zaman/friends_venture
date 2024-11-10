from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_column='CreatedAt', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='UpdatedAt', auto_now=True)
    active_status = models.BooleanField(db_column='ActiveStatus', default=True)

    class Meta:
        abstract = True