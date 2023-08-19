from django.shortcuts import render
from .models import Persons, Transactions
import json
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from datetime import date
from datetime import  timedelta

# Get the current date


def index(request):
	today = date.today()
	total_collection =0
	all_transactions = Transactions.objects.filter(date__date=today).order_by("-date")
	for t in all_transactions:
		total_collection=total_collection+t.amount
	context ={
		"collection":total_collection,
		"date":today,
		"transactions" :all_transactions,
	}
	return render(request,"book/index.html",context)

def register(request):
	if request.method == "POST":
		current_date = datetime.now()

		date=request.POST["date"]
		print("date id .....",date)
		date_string = date
		date_format = "%d-%m-%Y"

		# Convert the date string to a date object
		date = datetime.strptime(date_string, date_format).date()
		print("converted date id .....",date)

		next = request.POST["next"]
		previous = request.POST["previous"]

		if previous == "true":
			date = date - timedelta(days=1)
			print("Previous date:", date)

		if next == "true":
			date = date + timedelta(days=1)
			print("Next date:", date)

		all_transactions = Transactions.objects.filter(date__icontains=date).order_by("-date")
		context ={
			"date":date,
			"transactions" :all_transactions,
		}
		return render(request,"book/register.html",context)
	all_transactions = Transactions.objects.all().order_by("-date")
	date = datetime.now()
	context ={
		"date":date,
		"transactions" :all_transactions,
	}
	return render(request,"book/register.html",context)
def allperson(request):
	all_persons = Persons.objects.all()
	total = 0
	persons_data =[]
	for p in all_persons:
		total = 0
		t_all = Transactions.objects.filter(name=p)
		for t in t_all:
			print(p.name,t.borrow)
			total=total+t.borrow
		persons_data.append({
			"name":p.name,
			"borrow":total,

		})
	print(persons_data)

	context ={
		"persons" :persons_data,
	}
	return render(request,"book/persons.html",context)

def add_purchase(request):
	if request.method == "POST":
		name=request.POST["name"]
		amount=request.POST["amount"]
		borrow=request.POST["borrow"]
		if name=="":
			t = Transactions(amount=amount)
			t.save()
		else:
			t = Transactions(name=Persons.objects.get(name=name),amount=amount,borrow=-int(borrow))
			t.save()
		return redirect('book:index')

		# print(request.POST["name"] ,request.POST["amount"])

	names=[]
	pp = Persons.objects.all()
	for p in pp:
		names.append({"names":p.name})
	
	context = {
		"persons": json.dumps(names) 
	}

	return render(request,"book/add_purchase.html",context)

def add_person(request):
	if request.method == "POST":
		name=request.POST["name"]
		address=request.POST["address"]
		phone=request.POST["phone"]
		p = Persons(name=name,address=address,phone=phone)
		p.save()
	return render(request,"book/add_person.html")


def single_person_transactions(request,name):
	if request.method == "POST":

		amount=int(request.POST["amount"])
		print("amount is ",amount)
		p=Persons.objects.get(name=name)
		t_all= Transactions.objects.filter(name=p)
		for t in t_all:
			cur_borrow =int(t.borrow)
			print("curent borrow ",cur_borrow)
			if amount == 0:
				break

			if (cur_borrow<0):
				if ((amount + cur_borrow)>0):
					amount = amount + cur_borrow
					t.borrow = 0
					print("condi > ",t.borrow)
					t.save()
					continue

				if ((amount + cur_borrow)==0):
					amount = amount + cur_borrow
					t.borrow = 0
					print("condi == ",t.borrow)
					t.save()
					break

				if ((amount + cur_borrow)<0):
					t.borrow = amount + cur_borrow
					amount = 0
					print("condi < ",t.borrow)
					t.save()
					break


	p=Persons.objects.get(name=name)
	t_all= Transactions.objects.filter(name=p).order_by('-date')
	transactions = []
	for t in t_all:
		# print(t.amount)
		paid =0
		if int(t.borrow)<0:
			paid =0
		else:
			paid =1
			
		transactions.append({
			"date":t.date,
			"amount":t.amount,
			"borrow":t.borrow,
			"paid":paid
		})
	
	context={
		"name":p.name,
		"balance":p.account_balance,
		"transactions":transactions,
		"transaction_object":t_all
	}
	return render(request,"book/single_person_transactions.html",context)
def calculator(request):
	
	return render(request,"book/calculator.html")