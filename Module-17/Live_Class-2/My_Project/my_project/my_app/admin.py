from django.contrib import admin

from . import models                    # imported by me


# Register your models here.
admin.site.register(models.Blog)                # name of the model is blog