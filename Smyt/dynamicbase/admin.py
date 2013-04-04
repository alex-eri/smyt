import models
import django.db.models.base
from django.contrib import admin

models_dict= models.__dict__
my_models = filter( lambda k: type(models_dict[k]) == django.db.models.base.ModelBase, models_dict)

for k in my_models:
    admin.site.register(models_dict[k],admin.ModelAdmin)