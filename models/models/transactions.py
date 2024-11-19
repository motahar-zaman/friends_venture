from django.db import models
from .main import BaseModel


class Transaction(BaseModel):
    CREDIT_TYPE = 'credit'
    DEBIT_TYPE = 'debit'

    type_choices = [
        (CREDIT_TYPE, 'Credit'),
        (DEBIT_TYPE, 'Debit')
    ]

    partner = models.ForeignKey('Partner', db_column='Partner', on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(db_column='TransactionType', max_length=6, choices=type_choices)
    amount = models.PositiveBigIntegerField(db_column='Amount', default=0)
    date = models.DateField(db_column='TransactionDate', null=False)
    given_by = models.CharField(db_column='GivenBy', max_length=64, null=False)
    purpose = models.TextField(db_column='Purpose', null=True)
    updated_by = models.CharField(db_column='UpdatedBy', max_length=16, null=False)
    note = models.TextField(db_column='Note', null=True)

    def __str__(self):
        return f'{self.partner.nick_name}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'Transaction'
