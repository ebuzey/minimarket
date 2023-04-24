from django.contrib import admin
import main.models


# Register your models here.
admin.site.register(main.models.Category)
admin.site.register(main.models.Unit)
admin.site.register(main.models.Product)
