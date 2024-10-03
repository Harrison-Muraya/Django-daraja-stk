from django.db import models

# Create your models here.
from django.db import models

class MpesaTransaction(models.Model):
    phone_number = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.phone_number}"
