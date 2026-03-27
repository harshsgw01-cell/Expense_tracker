from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    date = models.DateField()  # ← removed auto_now_add so frontend can pass a date

    def __str__(self):
        return f"{self.user.username}: {self.description} - ₹{self.amount}"