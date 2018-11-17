from django.contrib import admin

from banner.models import banner, installment
# Register your models here.
myModels = [banner, installment]

admin.site.register(myModels)