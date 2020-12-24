from django.db import models
from django.db.models import Sum

class contributor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def totalcontribution(self):
        try:
            paid = payments.objects.filter(contributor__id=self.id).aggregate(Sum('amount'))
            return paid['amount__sum']
        except :
            return 0

    def __str__(self):
        return self.name

class paymentmode(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class contractor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class itemedBudget(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.DecimalField(default=0,max_digits=20,decimal_places=2)
    cost = models.DecimalField(default=0,max_digits=20,decimal_places=2)
    totalcost = models.DecimalField(default=0,max_digits=20,decimal_places=2)
    contractor = models.ManyToManyField(contractor,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def listcontractors(self):
        a = []
        for b in self.contractor.all():
            a.append(b.name)
        return a

    def paid(self):
        try:
            paid = payments.objects.filter(item__id=self.id).aggregate(Sum('amount'))
            print(paid)
            return paid['amount__sum']
        except :
            return 0

    def remainingbudget(self):
        try:
            return self.totalcost - self.paid()
        except :
            return 0

    def totalpaid(self):
        try:
            paid = payments.objects.all().aggregate(Sum('amount'))
            print(paid)
            return paid['amount__sum']
        except :
            return 0

    def totalremainingbudget(self):
        totalbudget = itemedBudget.objects.all().aggregate(Sum('totalcost'))
        try:
            return totalbudget['totalcost__sum'] - self.totalpaid()
        except :
            return 0

    def __str__(self):
        return self.name

class payments(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    contributor = models.ForeignKey(contributor, models.SET_NULL, blank=True, null=True)
    mode = models.ForeignKey(paymentmode, models.SET_NULL, blank=True, null=True)
    contractor = models.ForeignKey(contractor, models.SET_NULL, blank=True, null=True)
    item = models.ForeignKey(itemedBudget, models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(default=0,max_digits=20,decimal_places=2)

    def __str__(self):
        return self.name

