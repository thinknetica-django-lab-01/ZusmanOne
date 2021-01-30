from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models


from ckeditor.widgets import CKEditorWidget
from .models import Product,SaleMan
class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField : {'widget': CKEditorWidget}
    }
admin.site.unregister(FlatPage)
admin.site.register(FlatPage,FlatPageAdmin)
admin.site.register(Product)
admin.site.register(SaleMan)
# Register your models here.
