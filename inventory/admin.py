from django.contrib import admin
from .models import Section, Part, Delivery, Expense

admin.site.register(Section)
admin.site.register(Part)
admin.site.register(Delivery)
admin.site.register(Expense)