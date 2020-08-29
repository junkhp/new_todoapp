from django.contrib import admin
from .models import ToDoModel, HowtoOrder

# Register your models here.
admin.site.register(ToDoModel)
admin.site.register(HowtoOrder)
