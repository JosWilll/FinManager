from .models import *
from django.db.models import Sum
from decimal import Decimal


# Рахує всі витрати та всі внесення для статистики
def countExpInc(request):
  allExpenses = Transaction.objects.filter(isExpense=True)
  allIncomes = Transaction.objects.filter(isExpense=False)
  totalExp = allExpenses.aggregate(Sum('tsum'))['tsum__sum'] if allExpenses.exists() else 0
  totalInc = allIncomes.aggregate(Sum('tsum'))['tsum__sum'] if allIncomes.exists() else 0

  return {'totalExp': totalExp, 'totalInc': totalInc}


# Підраховує для графіку статистику з транзакцій
def countStatsGraph(request):
  expCatsLabels = []
  expCatsVals = []

  incCatsLabels = []
  incCatsVals = []

  expCatsColors = []
  incCatsColors = []

  for cat in Category.objects.filter(isExpense=True):
    expCatsLabels.append(cat.title)
    allCatExpenses = Transaction.objects.filter(category=cat.pk)
    if allCatExpenses.exists():
      expCatsVals.append(float(allCatExpenses.aggregate(Sum('tsum'))['tsum__sum']))
    else:
      expCatsVals.append(0)
    
    # Генерація випадкового кольору за допомогою геш-функції на основі назви категорії
    # 16777215 = #FFFFFF, найбільше значення в RGB в шістнадцятковій системі
    charsum = 0
    for c in cat.title:
      charsum += ord(c)
    expCatsColors.append('#' + hex(charsum * 10**9 % 16777215)[2:])   # [2:] бо hex() повертає рядок з '0x...'

  for cat in Category.objects.filter(isExpense=False):
    incCatsLabels.append(cat.title)
    allCatIncomes = Transaction.objects.filter(category=cat.pk)
    if allCatIncomes.exists():
      incCatsVals.append(float(allCatIncomes.aggregate(Sum('tsum'))['tsum__sum']))
    else:
      incCatsVals.append(0)
    # Аналогічно з попереднім циклом
    charsum = 0
    for c in cat.title:
      charsum += ord(c)
    incCatsColors.append('#' + hex(charsum * 10**9 % 16777215)[2:])

  return {'expCatsLabels': expCatsLabels,
  'expCatsVals': expCatsVals,
  'expCatsColors': expCatsColors,
  'incCatsLabels': incCatsLabels,
  'incCatsVals': incCatsVals,
  'incCatsColors': incCatsColors}
  
# Перераховує, скільки наразі грошей є в користувача
def calculateBalance(request):
  for acc in Account.objects.all():
    incomes = Transaction.objects.filter(account=acc.pk, isExpense=False)
    expenses = Transaction.objects.filter(account=acc.pk, isExpense=True)
    acc.balance = acc.startBalance

    if incomes.exists():
      acc.balance += Decimal(incomes.aggregate(Sum('tsum'))['tsum__sum'])
    if expenses.exists():
      acc.balance -= Decimal(expenses.aggregate(Sum('tsum'))['tsum__sum'])
    
    acc.save()
  
  allMoney = 0
  if Account.objects.all().exists():
    allMoney = Account.objects.all().aggregate(Sum('balance'))['balance__sum']
  return {'allMoney': allMoney}

