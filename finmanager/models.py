from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    isExpense = models.BooleanField(default=True)


class Check(models.Model):
    tSum = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    tDateTime = models.DateTimeField("Date of transaction", default=None)


class Account(models.Model):
    name = models.CharField(max_length=100)
    startBalance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    balance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    isHidden = models.BooleanField(default=False)
 

class Transaction(models.Model):
    tsum = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    isExpense = models.BooleanField(default=True)
    checkID = models.ForeignKey(Check, on_delete=models.CASCADE, blank=True, null=True)
    tDateTime = models.DateTimeField("Date of transaction", default=None)

    def delete(self, *args, **kwargs):
        if self.isExpense:
            self.account.balance += self.tsum
        else:
            self.account.balance -= self.tsum
        self.account.save()
        super().delete(*args, **kwargs)


class Transfer(models.Model):
  accFrom = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, related_name="account_from")
  accTo = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, related_name="account_to")
  amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)