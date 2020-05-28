from django.contrib import admin

from .models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display=['id','name','description']
#this admin class defines how the model info has to display in django admin interface.
admin.site.register(Board,BoardAdmin)