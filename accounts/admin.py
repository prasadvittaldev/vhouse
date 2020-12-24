from django.contrib import admin
from .models import *


class Acontributor(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ["name", "description", "totalcontribution"]

class Apaymentmode(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ["name", "description"]


class AitemedBudget(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = [ "name", "description", "quantity", "cost", "totalcost", "listcontractors", "paid", "remainingbudget", "totalpaid","totalremainingbudget", "completed" ]

class Apayments(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = [ "name", "description", "contributor","mode", "contractor", "item", "created", "amount" ]
    list_filter = (
        # ('created', DateRangeFilter),
        'item', 'contractor','mode','contributor'
    )


admin.site.register(contributor,Acontributor)
admin.site.register(paymentmode,Apaymentmode)
admin.site.register(contractor,Apaymentmode)
admin.site.register(itemedBudget,AitemedBudget)
admin.site.register(payments,Apayments)

# Register your models here.
