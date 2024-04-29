from django.db import models
from django.utils import timezone

from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# Create your models here.
class Persons(models.Model):
	name = models.CharField(max_length=300)#,validators=[alphanumeric]
	address = models.CharField(max_length=300,null=True,blank=True)
	phone = models.CharField(max_length=20,null=True,blank=True)
	account_balance = models.IntegerField(default=0,null=True,blank=True)

	def __str__(self):
		return str(self.id)
	

class Transactions(models.Model):
	date  = models.DateTimeField(default=timezone.now)
	name  = models.ForeignKey(Persons, on_delete=models.CASCADE, null=True,blank=True)
	amount = models.IntegerField(default=0)
	borrow = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id)
	

class Ipl(models.Model):
	name = models.CharField(max_length=300)#,validators=[alphanumeric]
	data = models.CharField(max_length=1000)#,validators=[alphanumeric]

	def __str__(self):
		return str(self.id)
	
class Team(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team2')

    def __str__(self):
        return f"{self.team1} vs {self.team2}"