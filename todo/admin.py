from django.contrib import admin
from .models import ToDoModel, CustomUser

# Register your models here.
admin.site.register(ToDoModel)
admin.site.register(CustomUser)
