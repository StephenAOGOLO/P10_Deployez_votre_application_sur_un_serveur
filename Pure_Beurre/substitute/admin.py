from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Users)
admin.site.register(Aliment)
admin.site.register(Category)
admin.site.register(Historic)