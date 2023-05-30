from django.contrib import admin
from app1.models import *


# Register your models here.
class blogregistor(admin.ModelAdmin):
    list_display = ['name','tagline']
    search_fields = ['name','tagline']


admin.site.register(Blog,blogregistor)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Catogory)