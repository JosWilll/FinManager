from rest_framework import routers, serializers, viewsets
from .models import *

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ['id', 'name', 'balance', 'isHidden']
    


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'title', 'isExpense']
  
  
class TransactionSerializer(serializers.ModelSerializer):
  checkID = serializers.PrimaryKeyRelatedField(
        queryset=Check.objects.all(),
        required=False,
        allow_null=True
    )

  class Meta:
    model = Transaction
    fields = ['id', 'tsum', 'category', 'account', 'comment', 'isExpense', 'checkID', 'tDateTime']
  

class TransferSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transfer
    fields = ['id', 'accFrom', 'accTo', 'amount']


class CheckSerializer(serializers.ModelSerializer):
  class Meta:
    model = Check
    fields = ['id', 'tSum', 'tDateTime']