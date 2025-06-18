from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.db.models import Sum
from django.shortcuts import get_object_or_404

from datetime import datetime

from .models import *
from .forms import *

from decimal import Decimal

import json

# Головна сторінка
def index(request):
		expDescending = {}
		incDescending = {}

		for cat in Category.objects.all():
				catTransactions = Transaction.objects.filter(category=cat.pk)
				if catTransactions.exists():
						catSum = float(catTransactions.aggregate(Sum('tsum'))['tsum__sum'])
				else:
						catSum = 0
				if cat.isExpense:
						expDescending[cat.title]= catSum
				else:
						incDescending[cat.title]= catSum
				
		context = {
				'expensesDescending': expDescending,
				'incomesDescending': incDescending,
		}

		return render(request, "finmanager/index.html", context)


# Accounts: GET
def accounts(request):
		context = {
				"accounts": Account.objects.all()
		}
		return render(request, "finmanager/accountsView.html", context)

# Accounts: POST
def accCreate(request):
		if request.method == "GET":
				context = {}
				return render(request, "finmanager/newAccView.html", context)
		
		if request.method == "POST":
				newAcc = Account(
						name=request.POST.get("name"),
						startBalance=float(request.POST.get("balance")),
						balance=float(request.POST.get("balance")),
						isHidden=request.POST.get("isHidden") == "hidden"
				)
				newAcc.save()
				return redirect("accounts")

# Accounts: PUT
def accEdit(request, pk):
		acc = get_object_or_404(Account, pk=pk)

		if request.method == "POST":
				balanceDiff = Decimal(request.POST.get("balance")) - acc.balance

				acc.name = request.POST.get("name")
				acc.startBalance += balanceDiff
				acc.isHidden = request.POST.get("isHidden") == "hidden"
				acc.save()
				return redirect("accounts")
		
		return render(request, "finmanager/newAccView.html", {"isEdit": True, "account": acc})

# Accounts: DELETE
def accDelete(request, pk):
		acc = get_object_or_404(Account, pk=pk)
		acc.delete()
		return redirect("accounts")


# Transactions: GET
def transactions(request):
		latest_transactions = Transaction.objects.order_by("tDateTime")

		context = {
				"latest_transactions": latest_transactions,
		}
		
		return render(request, "finmanager/transactionsView.html", context)

# Transactions: POST
def transCreate(request):
		if request.method == "GET": 
				context = {'isEdit': False}

				context["categoriesExp"] = Category.objects.filter(isExpense=True)
				context["categoriesInc"] = Category.objects.filter(isExpense=False)

				context["accounts"] = Account.objects.all()
		
				formTrans = TransactionForm()
				
				context['isExpense'] = 'exp' if request.GET.get("type", None) == 'expense' else 'inc'
				context['currDateTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

				return render(request, "finmanager/newTransView.html", context)
		
		if request.method == "POST":
				categoryCurrent = None  # Щоб новостворену категорію обрати

				# Якщо введено щось у поле для нової категорії, 
				# то створюємо цю категорію
				if request.POST.get("category") == "-1":
						newCatData = {
								"title": request.POST.get("newCatName"),
								"isExpense": bool(request.POST.get("isExpense") == "expense"),
						}
						formCat = CategoryForm(newCatData)
						if formCat.is_valid():
								categoryCurrent = formCat.save()
				else:
						categoryCurrent = Category.objects.get(pk=request.POST.get("category"))

				# Відбираємо дані з запиту, які необхідні для транзакції
				
				trans = Transaction()

				trans.account = Account.objects.get(pk=int(request.POST.get("account")))
				trans.tsum = Decimal(request.POST.get("tsum"))
				trans.isExpense = request.POST.get("isExpense") == "expense"
				trans.category = categoryCurrent
				trans.comment = request.POST.get("comment", "")
				trans.tDateTime = request.POST.get("tDateTime")

				trans.save()
				return redirect("transactions")

# Transaction PUT
def transEdit(request, pk):
		trans = get_object_or_404(Transaction, pk=pk)
		context = {"isEdit": True, "trans": trans}
		
		if request.method == "POST":
			categoryCurrent = None
			if request.POST.get("category") == "-1":
					newCatData = {
							"title": request.POST.get("newCatName"),
							"isExpense": bool(request.POST.get("isExpense") == "expense"),
					}
					formCat = CategoryForm(newCatData)
					if formCat.is_valid():
						categoryCurrent = formCat.save()
			else:
				categoryCurrent = Category.objects.get(pk=request.POST.get("category"))
 
				trans.account = Account.objects.get(pk=int(request.POST.get("account")))
				trans.tsum = Decimal(request.POST.get("tsum"))
				trans.isExpense = request.POST.get("isExpense") == "expense"
				trans.category = categoryCurrent
				trans.comment = request.POST.get("comment", "")
				trans.tDateTime = request.POST.get("tDateTime")

				trans.save()
				return redirect("transactions")
		
		if request.method == "GET": 

				context["categoriesExp"] = Category.objects.filter(isExpense=True)
				context["categoriesInc"] = Category.objects.filter(isExpense=False)

				context["accounts"] = Account.objects.all()
				context['isExpense'] = 'exp' if trans.isExpense else 'inc'
				context['currDateTime'] = datetime.now().strftime("%Y-%m-%dT%H:%M")
		return render(request, "finmanager/newTransView.html", context)

# Transactions DELETE
def transDelete(request, pk):
		trans = get_object_or_404(Transaction, pk=pk)
		trans.delete()
		return redirect("transactions")


# Categories GET
def categories(request):
		context = {
				"categories": Category.objects.order_by("isExpense"),
		}
		return render(request, "finmanager/categoriesView.html", context)

# Category POST
def catCreate(request):
		if request.method == "POST":
				newCat = Category(
						title=request.POST.get("title"),
						isExpense=request.POST.get("type")=='expense'
				)
				newCat.save()
				return redirect("categories")

# Category PUT
def catEdit(request, pk):
		if request.method == "POST":
				cat = get_object_or_404(Category, pk=pk)
				cat.title = request.POST.get("title")
				cat.isExpense = request.POST.get("type") == 'true'
				cat.save()
				catTransactions = Transaction.objects.filter(category=pk)
				for t in catTransactions:
						t.isExpense = cat.isExpense
						t.save()
				return redirect("categories")

# Category DELETE
def catDelete(request, pk):
		cat = get_object_or_404(Category, pk=pk)
		cat.delete()
		return redirect("categories")